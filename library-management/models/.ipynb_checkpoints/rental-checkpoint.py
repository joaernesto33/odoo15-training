# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Rental(models.Model):
    _name = 'academy.rental'
    _description = 'Rental Info'
    
    rental_code = fields.Char(string="Rental Code")
    customer_id = fields.Many2one(comodel_name='res.partner',
                               string='Customer',
                               ondelete='cascade',
                               required=True)
    
    books_ids = fields.One2many(comodel_name = 'book.copy', inverse_name = 'rental_id', string = 'Books')
    
    
    
    
    