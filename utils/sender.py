import requests

from utils.config import url
from utils.logger import logger


def send(json_body):
    headers = {'Content-Type': 'application/json'}
    logger.debug(f'Request body = {json_body}')
    return requests.post(url=url, headers=headers, data=json_body)
