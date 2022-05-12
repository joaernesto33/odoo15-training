# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage training""",
    
    'description': """
        Academy Module to manage training:
        -Courses
        -Sessions
        -Attendees
    """,
    
    'author': 'Jokin',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
    ],
    
    'demo': [
        'demo/academy_demo.xml',
        
    ],
    
    'license': 'OPL-1',
    'application': 'True',
    
}