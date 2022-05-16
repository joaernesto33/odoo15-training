# -*- coding: utf-8 -*-

{
    'name': 'Library Management',
    
    'summary': """Academy app to manage training""",
    
    'description': """
        Academy Module to manage customer checkings and organizing books:
        -Books
        -Customers
        -Rentals
    """,
    
    'author': 'Jokin',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menuitems.xml',
        'views/book_views.xml',
        'views/rental_views.xml',
    ],
    
    'demo': [
        'demo/book_demo.xml',
    ],
    
    'license': 'OPL-1',
    'application': 'True',
}