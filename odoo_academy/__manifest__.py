# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage Training""",
    
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees 
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
     'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/libro_views.xml'
         
     ],
    
    'demo': [
        'demo/academy_test.xml',
        'demo/academy_test2.xml',
    ],
    
    'license': 'OPL-1'
    
}