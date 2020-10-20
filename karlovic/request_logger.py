from bottle import request
from functools import wraps
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] {%(processName)s/%(threadName)s} %(asctime)s %(message)s',
)


def log():
    return logging.getLogger('kosmos-python-server')


def request_logger(fn):
    @wraps(fn)
    def _log(*args, **kwargs):
        actual_response = fn(*args, **kwargs)
        log().info(f'{request.method} {request.url}')

        return actual_response
    return _log
