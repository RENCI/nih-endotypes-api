# coding: utf-8

from __future__ import absolute_import

from server.models.body import Body
from server.models.inline_response200 import InlineResponse200
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_endotypes_get(self):
        """
        Test case for endotypes_get

        list of endotypes
        """
        body = Body()
        response = self.client.open('/v1/endotypes',
                                    method='GET',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()