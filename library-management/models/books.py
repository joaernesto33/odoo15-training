# -*- coding: utf-8 -*-*

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Book(models.Model):
    
    _name = 'academy.book'
    _description = 'Book Info'

    name = fields.Char(string='Title', required=True)
    authors = fields.Char(string='Authors', required=True)
    editors = fields.Char(string='Editors')
    publishers = fields.Char(string='Publishers')

    edition_year = fields.Integer(string='Year of Edition', required=True)
    
    isbn = fields.Char(string='ISBN')
    genre = fields.Char(string='Genre')
    
    notes = fields.Text(string="Notes")
    
    rental_id = fields.Many2one(comodel_name='academy.rental',
                               string='Rental',
                               ondelete='cascade')
    
    @api.onchange('isbn')
    def _onchange_isbn(self):
        if self.isbn:
            if len(self.isbn) != 13:
                raise ValidationError(f'The ISBN must be 13 characters long')
            
        
    