import functools

from tg import abort
from sqlalchemy.exc import IntegrityError

from eteamin.model import DBSession


def authorize():
    def wrapper(func):
        @functools.wraps(func)
        def wrapped(*args, **kw):
            return func(*args, **kw)
        return wrapped
    return wrapper


def flush():
    def wrapper(func):
        @functools.wraps(func)
        def wrapped(*args, **kw):
            result = func(*args, **kw)
            try:
                DBSession.flush()
                return result
            except IntegrityError:
                abort(400, detail='Bad Request!', passthrough='json')
        return wrapped
    return wrapper
