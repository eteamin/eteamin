from tg import expose
from tg.controllers.restcontroller import RestController

from eteamin.model import Tag


class TagController(RestController):

    @expose('json')
    def get_one(self, uid):
        return dict(tag=Tag.one_or_none(uid))

    def get_all(self):
        raise NotImplementedError

    @expose('json')
    def post(self):
        return dict(tag=Tag.from_request())

    def put(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
