from tg import request, abort

from eteamin.model import DBSession


class ConstructorMixin:
    @classmethod
    def one_or_none(cls, uid):
        instance = DBSession.query(cls).filter(cls.uid == uid).one_or_none()
        if not instance:
            abort(404, passthrough='json')
        return instance

    @classmethod
    def all(cls):
        return DBSession.query(cls).all()

    @classmethod
    def from_request(cls):
        data = request.json
        parent = cls()
        for k, v in cls.as_json().items():
            parent.__setattr__(k, data.get(k))
        DBSession.add(parent)
        return parent

    @classmethod
    def as_json(cls):
        raise NotImplementedError
