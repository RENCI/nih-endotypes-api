import connexion
import json
from models.input import Input
from models.inline_response200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from util import deserialize_date, deserialize_datetime


def endotypes_get(input):
    """
    list of endotypes
    :param input:
    :type input: dict | bytes

    :rtype: List[InlineResponse200]
    """
    if connexion.request.is_json:
        # for some reason connexion.request.get_json() returns null, need to figure out later
        input = Input.from_dict(connexion.request.get_json())
        # input values can be retrieved by
        # input.date_of_birth
        # input.race
        # input.sex
        # for v in input.visits:
        #    str += v.icd_code + ', ' + v.time + ', ' + v.visit_type + ', ' + v.zip
        #    str += v.exposure.value + ', ' + v.exposure.units + ', ' + v.exposure.exposure_type

        result = ''
        with open('results.json', 'r') as f:
            result = json.load(f)

        if result:
            ret_dict = {"input": connexion.request.get_json(),
                        "output": result}
        else:
            ret_dict = connexion.request.get_json()

        return ret_dict

    else:
        return "Please fill out a JSON request body as input before making the request."
