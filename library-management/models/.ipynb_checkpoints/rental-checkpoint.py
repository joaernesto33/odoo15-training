# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Rental(models.Model):
    _name = 'academy.rental'
    _description = 'Rental Info'
    
    customer_id = fields.Many2one(comodel_name='res.partner',
                               string='Customer',
                               ondelete='cascade',
                               required=True)
    
    books_ids = fields.One2many(comodel_name = 'academy.book', inverse_name = 'rental_id', string = 'Books')
    
    
    
    
    