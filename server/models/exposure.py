# coding: utf-8

from __future__ import absolute_import
from models.base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from util import deserialize_model


class Exposure(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, value: str=None, units: str=None, exposure_type: str=None):
        """
        Exposure - a model defined in Swagger

        :param value: The value of this Exposure.
        :type value: str
        :param units: The units of this Exposure.
        :type units: str
        :param exposure_type: The exposure_type of this Exposure.
        :type exposure_type: str
        """
        self.swagger_types = {
            'value': str,
            'units': str,
            'exposure_type': str
        }

        self.attribute_map = {
            'value': 'value',
            'units': 'units',
            'exposure_type': 'exposure_type'
        }

        self._value = value
        self._units = units
        self._exposure_type = exposure_type

    @classmethod
    def from_dict(cls, dikt) -> 'Exposure':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The exposure of this Exposure.
        :rtype: Exposure
        """
        return deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """
        Gets the value of this Exposure.

        :return: The value of this Exposure.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """
        Sets the value of this Exposure.

        :param value: The value of this Exposure.
        :type value: str
        """

        self._value = value

    @property
    def units(self) -> str:
        """
        Gets the units of this Exposure.

        :return: The units of this Exposure.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units: str):
        """
        Sets the units of this Exposure.

        :param units: The units of this Exposure.
        :type units: str
        """

        self._units = units

    @property
    def exposure_type(self) -> str:
        """
        Gets the exposure_type of this Exposure.

        :return: The exposure_type of this Exposure.
        :rtype: str
        """
        return self._exposure_type

    @exposure_type.setter
    def exposure_type(self, exposure_type: str):
        """
        Sets the exposure_type of this Exposure.

        :param exposure_type: The exposure_type of this Exposure.
        :type exposure_type: str
        """

        self._exposure_type = exposure_type

