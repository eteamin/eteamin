# -*- coding: utf-8 -*-
from eteamin.tests import TestController


class TestPost(TestController):

    def test_tag(self):
        """Testing Posing Tag"""
        payload = {
            'title': 'this is a title',
        }
        post_resp = self.app.post_json('/api/tags', params=payload).json

        get_resp = self.app.get('/api/tags/{}'.format(post_resp['tag'].get('uid'))).json

        assert payload.get('title') == get_resp['tag'].get('title')

        payload = {
            'title': None
        }
        self.app.post_json('/api/tags/', payload, status=400)

        payload = {}
        self.app.post_json('/api/tags', payload, status=400)
