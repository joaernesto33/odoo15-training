# -*- coding: utf-8 -*-

{
    'name': 'Space Mission',
    
    'summary': """Academy app to manage training""",
    
    'description': """
        Academy Module to manage space mission logistics:
        -Planning
        -Spaceship
        -Space crew
    """,
    
    'author': 'Jokin',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/space_security.xml',
        'security/ir.model.access.csv',
        'views/space_menuitems.xml',
    ],
    
    'demo': [
        'demo/spaceship_demo.xml',
        
    ],
    
    'license': 'OPL-1',
    'application': 'True',
}