import connexion
import json
import re
from models.input import Input
from models.exposure import Exposure
from models.response200 import Response200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from util import deserialize_date, deserialize_datetime
from flask import Response


def validate_exposure_type_and_units(ex_type, ex_unit):
    supported_units = {'pm25': 'ugm3', 'o3': 'ppm'}
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

def validate_lat_lon(lat, lon):
    if lat is None:
        return 'Invalid Parameter', 400, {'error': "latitude cannot be empty"}
    if lon is None:
        return 'Invalid Parameter', 400, {'error': "longitude cannot be empty"}

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
        for v in input.visits:
            error, status, dict = validate_lat_lon(v.lat, v.lon)
            if status != 200:
                return error, status, dict

            error, status, dict = validate_exposure_type_and_units(v.exposure.exposure_type,
                                                                   v.exposure.units)
            if status != 200:
                return error, status, dict

            error, status, dict = validate_icd_codes(v.icd_codes)
            if status != 200:
                return error, status, dict

        # input values can be retrieved by
        # input.date_of_birth
        # input.race
        # input.sex
        # for v in input.visits:
        #    str += v.icd_codes + ', ' + v.time + ', ' + v.visit_type + ', ' + v.lat + ', ' + v.lon
        #    str += v.exposure.value + ', ' + v.exposure.units + ', ' + v.exposure.exposure_type

        result = ''
        with open('results.json', 'r') as f:
            result = json.load(f)

        if result:
            ret_dict = {"output": result}
        else:
            ret_dict = connexion.request.get_json()

        return ret_dict

    else:
        return 'Invalid Parameter', 400, {'error': "Please fill out a JSON request body as input "
                                                   "before making the request."}
