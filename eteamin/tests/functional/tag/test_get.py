# -*- coding: utf-8 -*-
from eteamin.tests import TestController


class TestGet(TestController):
    def setUp(self):
        super(TestGet, self).setUp()
        self.payload = {
            'title': 'this is a title',
        }
        self.post_resp = self.app.post_json('/api/tags', params=self.payload).json

    def test_tag(self):
        """Testing Getting Tag"""
        get_resp = self.app.get('/api/tags/{}'.format(self.post_resp['tag'].get('uid'))).json

        assert self.payload.get('title') == get_resp['tag'].get('title')

        self.app.get('/api/tags/{}'.format(2132423), status=404)
