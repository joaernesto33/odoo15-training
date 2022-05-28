#-*- coding: utf-8 -*-
from odoo import models, fields, api

class Volunteer(models.Model):
    _inherit = 'res.partner'
    
    tasks_ids = fields.Many2many(comodel_name='academy.task', string='Tasks')