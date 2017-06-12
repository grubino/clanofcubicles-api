import connexion
from clashofcubicles.models.api_response import ApiResponse
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def create_task(body):
    """
    create task
    create task
    :param body: task to create
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ApiResponse.from_dict(connexion.request.get_json())
    return 'do some magic!'


def get_task(filter=None):
    """
    get tasks
    get tasks
    :param filter: filter results
    :type filter: str

    :rtype: None
    """
    return 'do some magic!'


def get_task_by_id(taskId):
    """
    get task by id
    get task by id
    :param taskId: task id
    :type taskId: str

    :rtype: None
    """
    return 'do some magic!'
