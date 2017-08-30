from tg import request

from eteamin.model import DBSession


class ConstructorMixin:
    @classmethod
    def one_or_none(cls, uid):
        return DBSession.query(cls).filter(cls.uid == uid).one_or_none()

    @classmethod
    def from_request(cls):
        data = request.json
        parent = cls()
        for k, v in cls.as_json().items():
            parent.__setattr__(k, data.get(k))
        DBSession.add(parent)
        DBSession.flush()
        return parent

    @classmethod
    def as_json(cls):
        raise NotImplementedError
