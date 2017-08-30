from tg import expose
from tg.controllers.restcontroller import RestController

from eteamin.model import Tag
from eteamin.lib.decorators import flush


class TagController(RestController):

    @expose('json')
    def get_one(self, uid):
        return dict(tag=Tag.one_or_none(uid))

    @expose('json')
    def get_all(self):
        return dict(tags=Tag.all())

    @expose('json')
    @flush()
    def post(self):
        return dict(tag=Tag.from_request())

    def put(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
