# coding: utf-8

from __future__ import absolute_import

from clashofcubicles.models.api_response import ApiResponse
from clashofcubicles.models.worker import Worker
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestWorkersController(BaseTestCase):
    """ WorkersController integration test stubs """

    def test_add_worker(self):
        """
        Test case for add_worker

        create a worker
        """
        body = Worker()
        response = self.client.open('/v1/workers',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_worker(self):
        """
        Test case for delete_worker

        Deletes a worker
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open('/v1/workers/{workerId}'.format(workerId=789),
                                    method='DELETE',
                                    headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_worker_by_id(self):
        """
        Test case for get_worker_by_id

        Find worker by ID
        """
        response = self.client.open('/v1/workers/{workerId}'.format(workerId=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_worker(self):
        """
        Test case for update_worker

        Update an existing worker
        """
        body = Worker()
        headers = [('api_key', 'api_key_example')]
        response = self.client.open('/v1/workers',
                                    method='PUT',
                                    data=json.dumps(body),
                                    headers=headers,
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
