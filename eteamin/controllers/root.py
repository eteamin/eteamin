# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context, abort
from tg.exceptions import HTTPFound
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from eteamin.lib.base import BaseController
from eteamin.controllers.error import ErrorController
from eteamin import model
from eteamin.model import DBSession


__all__ = ['RootController', 'APIController']


class APIController(BaseController):
    pass


class RootController(BaseController):
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)
    error = ErrorController()
    api = APIController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "eteamin"

    @expose('eteamin.templates.index')
    def index(self):
        abort(404)

    @expose('eteamin.templates.login')
    def login(self, came_from=lurl('/'), failure=None, login=''):
        return dict(page='login')

    @expose()
    def post_login(self, came_from=lurl('/')):
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                     params=dict(came_from=came_from, __logins=login_counter))
        return HTTPFound(location=came_from)
