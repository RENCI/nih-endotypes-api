import connexion
import json
from models.body import Body
from models.inline_response200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from util import deserialize_date, deserialize_datetime


def endotypes_get(body=None):
    """
    list of endotypes
    :param body:
    :type body: dict | bytes

    :rtype: List[InlineResponse200]
    """
    if connexion.request.is_json:
        # for some reason connexion.request.get_json() returns null, need to figure out later
        body = Body.from_dict(connexion.request.get_json())
        #if connexion.request.get_json():
        #    return json.dumps(connexion.request.get_json())
        #else:
        #    return "Null"
        with open('results.json', 'r') as f:
            data = json.load(f)
            return json.dumps(data)
