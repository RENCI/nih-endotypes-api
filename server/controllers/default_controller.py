import connexion
import json
import re
import subprocess
from models.input import Input
from models.exposure import Exposure
from models.response200 import Response200
import datetime
from typing import List, Dict
from six import iteritems
from util import deserialize_date, deserialize_datetime
from flask import Response


def validate_exposure_type_and_units(exs = []):
    supported_units = {'pm25': 'ugm3', 'o3': 'ppm'}
    for ex in exs:
        ex_type = ex.exposure_type
        ex_unit = ex.units
        if ex_type is None:
            return 'Invalid Parameter', 400, {'error': 'exposure_type cannot be empty'}

        if ex_unit is None:
            return 'Invalid Parameter', 400, {'error': 'exposure units cannot be empty'}

        if ex_type.lower() not in supported_units.keys():
            print (ex_type + ', ' + ex_unit + '.......Updated')
            return 'Invalid Parameter', 400, {'error': 'exposure types must be pm25 or o3'}

        if ex_unit.lower() != supported_units[ex_type]:
            return 'Invalid Parameter', 400, {'error': 'Invalid value for exposure unit, must be ugm3 '
                                                       'for pm25 exposure type or ppm for o3 exposure type'}

    return 'OK', 200, 'OK'

def validate_date_of_birth(date):
    if date is None:
        return 'Invalid Parameter', 400, {'error': 'date_of_birth cannot be empty'}

    try:
        valid_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        today_date = str(datetime.date.today())
        if date >= today_date:
            return 'Invalid Parameter', 400, {'error': 'date_of_birth cannot be a future date'}
    except ValueError as ex:
        return 'Invalid Parameter', 400, {'error': ex}

    return 'OK', 200, 'OK'

def validate_time(time):
    if time is None:
        return 'Invalid Parameter', 400, {'error': 'time cannot be empty'}

    try:
        valid_time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    except ValueError as ex:
        return 'Invalid Parameter', 400, {'error': ex}

    return 'OK', 200, 'OK'

def validate_lat_lon(lat, lon):
    if lat is None:
        return 'Invalid Parameter', 400, {'error': 'latitude cannot be empty'}
    if lon is None:
        return 'Invalid Parameter', 400, {'error': 'longitude cannot be empty'}

    # check latitude
    if re.match("^(\+|-)?(?:90(?:(?:\.0{1,})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,})?))$", lat) is None:
        return 'Invalid Parameter', 400, {'error': 'Invalid latitude'}

    # check longitude
    if re.match("^(\+|-)?(?:180(?:(?:\.0{1,})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,})?))$", lon) is None:
        return 'Invalid Parameter', 400, {'error': 'Invalid longitude'}

    return 'OK', 200, 'OK'

def validate_icd_codes(codes):
    if codes is not None:
        code_strs = codes.split(',')
        icd9_re = '(icd|ICD)9:(V\d{2}(\.\d{1,2})?|\d{3}(\.\d{1,2})?|E\d{3}(\.\d)?)'
        icd10_re = '(icd|ICD)10:[A-TV-Z][0-9][A-Z0-9](\.[A-Z0-9]{1,4})?'
        re_str = '^' + icd9_re + '|' + icd10_re + '$'
        for cstr in code_strs:
            cstr = cstr.strip()
            if not re.match(re_str, cstr):
                return 'Invalid Parameter', 400, \
                       {'error': "Invalid value for icd_codes, must be comma separated and "
                                 "conforming to ICD9 or ICD10 standard"}

    return 'OK', 200, 'OK'


def endotypes_post(input):
    """
    Get list of endotypes based on input as a POST request
    list of endotypes based on input that returns array of predicted endotypes
    :param input:
    :type input: dict | bytes

    :rtype: List[Response200]
    """
    if connexion.request.is_json:
        input = Input.from_dict(connexion.request.get_json())
        error, status, dict = validate_date_of_birth(input.date_of_birth)
        if status != 200:
            return error, status, dict

        for v in input.visits:
            error, status, dict = validate_lat_lon(v.lat, v.lon)
            if status != 200:
                return error, status, dict

            error, status, dict = validate_exposure_type_and_units(v.exposures)
            if status != 200:
                return error, status, dict

            error, status, dict = validate_icd_codes(v.icd_codes)
            if status != 200:
                return error, status, dict

            error, status, dict = validate_time(v.time)
            if status != 200:
                return error, status, dict

        # write request input json to r-models/input.json for model to consume
        input_data = {}
        input_data['date_of_birth'] = str(input.date_of_birth)
        input_data['race'] = input.race
        input_data['sex'] = input.sex
        input_data['model_type'] = input.model_type
        visit_list = []
        for v in input.visits:
            visit_dict = {}
            visit_dict['visit_type'] = v.visit_type
            visit_dict['time'] = str(v.time)
            visit_dict['lat'] = float(v.lat)
            visit_dict['lon'] = float(v.lon)

            code_list = []
            code_strs = v.icd_codes.split(',')
            for cstr in code_strs:
                cstr = cstr.strip()
                code_list.append(cstr)
            visit_dict['icd_codes'] = code_list
            ex_list = []
            for ex in v.exposures:
                exp_dict = {
                    'exposure_type': ex.exposure_type,
                    'units': ex.units,
                    'value': ex.value
                }
                ex_list.append(exp_dict)
            visit_dict['exposures'] = ex_list
            visit_list.append(visit_dict)

        input_data['visits'] = visit_list

        with open('r-model/input.json', 'w') as f:
            f.write(json.dumps(input_data, indent=4))

        # invoke r-script for model-generated decision tree for creating endotypes output
        proc = subprocess.Popen(['sh', 'run-r-model.sh'], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        if proc.returncode:
            return 'server error', 500, {'error': stderr}
        else:
            result = ''
            with open('r-model/output.json', 'r') as f:
                result = json.load(f)

            if result:
                if 'error' in result:
                    if result['error'][-1] == '\n':
                        result['error'] = result['error'][0:-1]
                    return 'server error', 500, {'error': result['error']}
                else:
                    ret_dict = {"output": result}
            else:
                ret_dict = {"input": connexion.request.get_json()}

            return ret_dict

    else:
        return 'Invalid Parameter', 400, {'error': "Please fill out a JSON request body as input "
                                                   "before making the request."}
