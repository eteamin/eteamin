# -*- coding: utf-8 -*-

from eteamin.tests import TestController
from eteamin.tests.functional.article import IMAGE


class TestPostArticle(TestController):
    def setUp(self):
        super(TestPostArticle, self).setUp()

    def test_post(self):
        """Testing Posting Article"""
        with open(IMAGE, 'rb') as image:
            files = [('image', 'image.jpg', image.read())]
        payload = {
            'title': 'this is a title',
            'text': 'this is a text'
        }
        post_resp = self.app.post('/api/articles', params=payload, upload_files=files).json

        get_resp = self.app.get('/api/articles/{}'.format(post_resp['article'].get('uid'))).json

        assert get_resp['article'].get('views') == 1
