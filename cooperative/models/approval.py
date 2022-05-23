# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Approval(models.Model):
    _inherit = 'approval.request'
    
    task_id = fields.Many2one(comodel_name='academy.task',
                                string='Related Task',
                                ondelete='set null')