import random
import time
import requests
from celery.signals import task_postrun
from celery.utils.log import get_task_logger
from cli import celery, db
from cli.models import User
from sqlalchemy import exc

logger = get_task_logger(__name__)


@celery.task(max_retries=3)
def sum_numbers(a, b):
    return a + b


