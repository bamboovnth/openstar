# -*- coding: utf-8 -*-
from odoo import http

# class Openstar(http.Controller):
#     @http.route('/openstar/openstar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openstar/openstar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openstar.listing', {
#             'root': '/openstar/openstar',
#             'objects': http.request.env['openstar.openstar'].search([]),
#         })

#     @http.route('/openstar/openstar/objects/<model("openstar.openstar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openstar.object', {
#             'object': obj
#         })