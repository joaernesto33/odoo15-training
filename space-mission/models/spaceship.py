# -*- coding: utf-8 -*-*

from odoo import models, fields, api, _

class Spaceship(models.Model):
    
    _name = 'academy.spaceship'
    _description = 'Spaceship Info'

    name = fields.Char(string='Title', required=True)
    ship_dimensions = fields.Text(string='Ship dimensions')
    fuel_type = fields.Char(string='Fuel type', required=True)
    ship_type = fields.Char(string='Ship type')
    number_passengers = fields.Integer(string='Number of Passengers', required=True)
    
    
    active = fields.Boolean(string='Active', default=True)