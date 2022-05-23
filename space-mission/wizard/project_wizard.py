# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectWizard(models.TransientModel):
    _name = 'academy.project.wizard'
    _description = 'Wizard: Quick Project for Space Missions'
    
    def _default_mission(self):
        return self.env['academy.mission'].browse(self._context.get('active_id'))
    
    mission_id = fields.Many2one(comodel_name='academy.mission',
                                 string='Mission',
                                 required=True,
                                 default=_default_mission)
    
    
    def create_project(self):
        
        order_id = self.env['project.project'].create({
            'name': self.mission_id.mission_name,
        })