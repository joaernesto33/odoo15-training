# -*- coding: utf-8 -*-*

from odoo import models, fields, api, _

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
    