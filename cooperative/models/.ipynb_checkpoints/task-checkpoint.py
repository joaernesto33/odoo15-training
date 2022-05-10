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
    
    
    
    
    
    