# coding: utf-8

from __future__ import absolute_import
from models.exposure import Exposure
from models.base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from util import deserialize_model


class Visit(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, time: str=None, zip: str=None, visit_type: str=None, icd_code: str=None, exposure: Exposure=None):
        """
        Visit - a model defined in Swagger

        :param time: The time of this Visit.
        :type time: str
        :param zip: The zip of this Visit.
        :type zip: str
        :param visit_type: The visit_type of this Visit.
        :type visit_type: str
        :param icd_code: The icd_code of this Visit.
        :type icd_code: str
        :param exposure: The exposure of this Visit.
        :type exposure: Exposure
        """
        self.swagger_types = {
            'time': str,
            'zip': str,
            'visit_type': str,
            'icd_code': str,
            'exposure': Exposure
        }

        self.attribute_map = {
            'time': 'time',
            'zip': 'zip',
            'visit_type': 'visit_type',
            'icd_code': 'icd_code',
            'exposure': 'exposure'
        }

        self._time = time
        self._zip = zip
        self._visit_type = visit_type
        self._icd_code = icd_code
        self._exposure = exposure

    @classmethod
    def from_dict(cls, dikt) -> 'Visit':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The visit of this Visit.
        :rtype: Visit
        """
        return deserialize_model(dikt, cls)

    @property
    def time(self) -> str:
        """
        Gets the time of this Visit.

        :return: The time of this Visit.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time: str):
        """
        Sets the time of this Visit.

        :param time: The time of this Visit.
        :type time: str
        """

        self._time = time

    @property
    def zip(self) -> str:
        """
        Gets the zip of this Visit.

        :return: The zip of this Visit.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip: str):
        """
        Sets the zip of this Visit.

        :param zip: The zip of this Visit.
        :type zip: str
        """

        self._zip = zip

    @property
    def visit_type(self) -> str:
        """
        Gets the visit_type of this Visit.

        :return: The visit_type of this Visit.
        :rtype: str
        """
        return self._visit_type

    @visit_type.setter
    def visit_type(self, visit_type: str):
        """
        Sets the visit_type of this Visit.

        :param visit_type: The visit_type of this Visit.
        :type visit_type: str
        """

        self._visit_type = visit_type

    @property
    def icd_code(self) -> str:
        """
        Gets the icd_code of this Visit.

        :return: The icd_code of this Visit.
        :rtype: str
        """
        return self._icd_code

    @icd_code.setter
    def icd_code(self, icd_code: str):
        """
        Sets the icd_code of this Visit.

        :param icd_code: The icd_code of this Visit.
        :type icd_code: str
        """

        self._icd_code = icd_code

    @property
    def exposure(self) -> Exposure:
        """
        Gets the exposure of this Visit.

        :return: The exposure of this Visit.
        :rtype: Exposure
        """
        return self._exposure

    @exposure.setter
    def exposure(self, exposure: Exposure):
        """
        Sets the exposure of this Visit.

        :param exposure: The exposure of this Visit.
        :type exposure: Exposure
        """

        self._exposure = exposure

