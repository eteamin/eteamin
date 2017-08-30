from tg import expose
from tg.controllers.restcontroller import RestController

from eteamin.model import Article
from eteamin.lib.decorators import flush


class ArticleController(RestController):

    @expose('json')
    @flush()
    def get_one(self, uid):
        return dict(article=Article.one_or_none(uid))

    @expose('json')
    def get_all(self):
        return dict(articles=Article.all())

    @expose('json')
    @flush()
    def post(self):
        return dict(article=Article.from_request())

    def put(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
