# coding: utf-8

from __future__ import absolute_import

from clashofcubicles.models.api_response import ApiResponse
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestTaskController(BaseTestCase):
    """ TaskController integration test stubs """

    def test_create_task(self):
        """
        Test case for create_task

        create task
        """
        body = ApiResponse()
        response = self.client.open('/v1/task',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_task(self):
        """
        Test case for get_task

        get tasks
        """
        query_string = [('filter', 'filter_example')]
        response = self.client.open('/v1/task',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_task_by_id(self):
        """
        Test case for get_task_by_id

        get task by id
        """
        response = self.client.open('/v1/task/{taskId}'.format(taskId='taskId_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
