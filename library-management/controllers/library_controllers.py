#-*- coding: utf-8 -*-

from odoo import http

class Library(http.Controller):
    @http.route('/library/', auth='public', website=True)
    def index(self, **kw):
        return "Hello, world"
    
    @http.route('/library/books/', auth='public', website=True)
    def books(self, **kw):
        books = http.request.env['academy.book'].search([])
        return http.request.render('library-management.books_website',{
            'books': books,
        })
    
    