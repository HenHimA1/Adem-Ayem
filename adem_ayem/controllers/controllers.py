# -*- coding: utf-8 -*-
# from odoo import http


# class Project\kosong\ademAyem(http.Controller):
#     @http.route('/project\kosong\adem_ayem/project\kosong\adem_ayem', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project\kosong\adem_ayem/project\kosong\adem_ayem/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project\kosong\adem_ayem.listing', {
#             'root': '/project\kosong\adem_ayem/project\kosong\adem_ayem',
#             'objects': http.request.env['project\kosong\adem_ayem.project\kosong\adem_ayem'].search([]),
#         })

#     @http.route('/project\kosong\adem_ayem/project\kosong\adem_ayem/objects/<model("project\kosong\adem_ayem.project\kosong\adem_ayem"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project\kosong\adem_ayem.object', {
#             'object': obj
#         })
