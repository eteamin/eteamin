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
        instance = cls()
        for k, v in cls.as_json().items():
            instance.__setattr__(k, data.get(k))
        DBSession.add(instance)
        return instance

    @classmethod
    def as_json(cls):
        raise NotImplementedError
