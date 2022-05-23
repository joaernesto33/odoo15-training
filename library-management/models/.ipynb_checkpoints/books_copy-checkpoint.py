# -*- coding: utf-8 -*-*

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class BookCopy(models.Model):
    
    _name = 'book.copy'
    _description = 'Book Copy Info'
    
    _inherits = {
        'academy.book': 'book_id',
    }

    unique_identifier = fields.Char(string='Identifier', required=True)
    book_id = fields.Many2one('academy.book', required=True, ondelete="cascade")

    
   