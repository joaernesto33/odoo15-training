# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'
    
    mission_id = fields.Many2one(comodel_name='academy.mission',
                                string='Related Mission',
                                ondelete='set null')