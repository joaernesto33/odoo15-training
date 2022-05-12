# -*- coding: utf-8 -*-

{
    'name': 'Cooperative Volunteers',
    
    'summary': """Academy app to manage training""",
    
    'description': """
        Academy Module to manage non-profit organisation:
        -Volunteers
        -Cooperative shops
        -Local products
    """,
    
    'author': 'Jokin',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/cooperative_security.xml',
        'security/ir.model.access.csv',
        'views/cooperative_menuitems.xml',
    ],
    
    'demo': [
        'demo/task_demo.xml',
    ],
    
    'license': 'OPL-1',
    'application': 'True',
}