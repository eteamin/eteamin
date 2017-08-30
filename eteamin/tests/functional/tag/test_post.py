# -*- coding: utf-8 -*-
from nose.tools import ok_

from eteamin.tests import TestController


class TestPost(TestController):

    def test_tag(self):
        payload = {
            'title': 'this is a title',
        }
        post_resp = self.app.post_json('/api/tags', params=payload).json

        get_resp = self.app.get('/api/tags/{}'.format(post_resp['tag'].get('uid'))).json

        assert payload.get('title') == get_resp['tag'].get('title')
