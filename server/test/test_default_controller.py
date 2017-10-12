# coding: utf-8

from __future__ import absolute_import

from server.models.input import Input
from server.models.response200 import Response200
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_endotypes_post(self):
        """
        Test case for endotypes_post

        Get list of endotypes based on input as a POST request
        """
        input = Input()
        response = self.client.open('/v1/endotypes',
                                    method='POST',
                                    data=json.dumps(input),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
