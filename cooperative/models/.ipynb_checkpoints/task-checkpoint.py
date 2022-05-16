# -*- coding: utf-8 -*-*

from odoo import models, fields, api, _

class Task(models.Model):
    
    _name = 'academy.task'
    _description = 'Task Info'

    task_name = fields.Char(string='Task name', required=True)
    description = fields.Text(string='Task description')
    task_type = fields.Char(string='Task Type')
    
    start_time = fields.Datetime(string='Task start time', required=True)
    stop_time = fields.Datetime(string='Task stop time', required=True)
    
    repeatable = fields.Boolean(string='Repeatable', default=True)
    
    task_state = fields.Selection(string='State', selection=[('draft', 'Draft'),
                                                             ('ready', 'Ready'),
                                                             ('inprogress', 'In-progress'),
                                                             ('done', 'Done')])
    
    leader_name = fields.Char(string="Leader's Name")
    
    task_volunteers = fields.Many2many(comodel_name='res.partner', string='Volunteers')
    
    @api.onchange('leader_name')
    def _onchange_leader(self):
        if self.leader_name == "":
            self.task_state = 'draft'
        else:
            self.task_state = 'ready'
    
    
    
    
    
    