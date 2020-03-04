# -*- coding: utf-8 -*-
{
    'name': "academy",

    'summary': """Manage trainings""",

    'description': """
       Open Academy module for managing trainings:
           - training courses
           - training sessions
           - attendees registration
   """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full listUncategorized
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'website','account',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/academy_views.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/reports.xml',
        'views/session_board.xml',
        'views/session_wizard.xml',
        'views/partner_views.xml',
        'views/teacher_views.xml',
        'views/templates.xml',
        'views/views.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
