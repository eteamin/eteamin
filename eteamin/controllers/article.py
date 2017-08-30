from tg.controllers.restcontroller import RestController


class ArticleController(RestController):

    def get_one(self):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def post(self):
        raise NotImplementedError

    def put(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
