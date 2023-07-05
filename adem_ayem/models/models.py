# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class project\kosong\adem_ayem(models.Model):
#     _name = 'project\kosong\adem_ayem.project\kosong\adem_ayem'
#     _description = 'project\kosong\adem_ayem.project\kosong\adem_ayem'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
