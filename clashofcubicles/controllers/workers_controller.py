import connexion
from clashofcubicles.models.api_response import ApiResponse
from clashofcubicles.models.worker import Worker
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_worker(body):
    """
    create a worker
    create a worker
    :param body: new worker object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Worker.from_dict(connexion.request.get_json())
    return 'do some magic!'


def delete_worker(workerId, api_key=None):
    """
    Deletes a worker
    
    :param workerId: worker id to delete
    :type workerId: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_worker_by_id(workerId):
    """
    Find worker by ID
    Returns a single worker
    :param workerId: ID of worker to return
    :type workerId: int

    :rtype: Worker
    """
    return 'do some magic!'


def update_worker(api_key, body):
    """
    Update an existing worker
    
    :param api_key: 
    :type api_key: str
    :param body: worker to update
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Worker.from_dict(connexion.request.get_json())
    return 'do some magic!'
