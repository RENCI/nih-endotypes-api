import connexion
from models.body import Body
from models.inline_response200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from util import deserialize_date, deserialize_datetime


def endotypes_get(body=None):
    """
    list of endotypes
    list of endotypes
    :param body: 
    :type body: dict | bytes

    :rtype: List[InlineResponse200]
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())
    return 'do some magic!'
