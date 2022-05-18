# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mission(models.Model):
    _name = 'academy.mission'
    _description = 'Mission Info'
    
    spaceship_id = fields.Many2one(comodel_name='academy.spaceship',
                               string='Spaceship',
                               ondelete='cascade',
                               required=True)
    
    mission_name = fields.Char(string='Title')
    launch_date = fields.Datetime(string='Launch Date', required=True)
    return_date = fields.Datetime(string='Return Date', required=True)
    
    crew_members = fields.Many2many(comodel_name='res.partner', string='Crew Members')
    
    fuel_amount = fields.Float(string="Amount of Fuel")
    engines = fields.Integer(string="Number of Engines")
    safety_features = fields.Integer(string="Safety Features")