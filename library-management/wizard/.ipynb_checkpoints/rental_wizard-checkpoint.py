# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RentalWizard(models.TransientModel):
    _name = 'academy.rental.wizard'
    _description = 'Wizard: Rental for Customers'
    
    def _default_book(self):
        return self.env['academy.book'].browse(self._context.get('active_id'))
    
    book_id = fields.Many2one(comodel_name='academy.book',
                                 string='Book',
                                 required=True,
                                 default=_default_book)
    
    customer_id = fields.Many2one(comodel_name='res.partner',
                                 string='Customer')
    
    rental_ids = fields.Many2one(comodel_name='academy.rental',
                                          string='Rentals with current book',
                                          related='book_id.rental_id',
                                          help='These are the rentals currently qith this book and customer')
    
    