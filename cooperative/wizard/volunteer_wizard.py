# -*- coding: utf-8 -*-

from odoo import models, fields, api

class VolunteerWizard(models.TransientModel):
    _name = 'academy.volunteer.wizard'
    _description = 'Wizard: Quick Volunteers for Tasks'
    
    def _default_volunteer(self):
        return self.env['res.partner'].browse(self._context.get('active_id'))
    
    volunteer_id = fields.Many2one(comodel_name='res.partner',
                                 string='Volunteer',
                                 required=True,
                                 default=_default_volunteer)
    
    
    task_ids = fields.Many2many(comodel_name='academy.task',
                                   string='Tasks for Volunteers')
    
    
    def write_task(self):
        for task in self.task_ids:
            task.write({
                'task_volunteers':self.volunteer_id,
            })
        