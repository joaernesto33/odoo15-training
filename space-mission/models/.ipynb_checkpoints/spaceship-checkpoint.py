# -*- coding: utf-8 -*-*

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Spaceship(models.Model):
    
    _name = 'academy.spaceship'
    _description = 'Spaceship Info'

    name = fields.Char(string='Title', required=True)
    ship_dimensions = fields.Text(string='Ship dimensions')
    
    width = fields.Float(string='Width', default=0.00)
    length = fields.Float(string='Length', default=0.00)
    
    fuel_type = fields.Char(string='Fuel type', required=True)
    ship_type = fields.Char(string='Ship type')
    number_passengers = fields.Integer(string='Number of Passengers', required=True)
    
    
    active = fields.Boolean(string='Active', default=True)
    
    @api.constrains('width', 'length')
    def _check_width_or_length(self):
        for record in self:
            if record.width > record.length:
                raise UserError(f'The width cannot be larger than the length')