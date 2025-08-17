# -*- coding: utf-8 -*-
{
    'name': "My Library",
    'summary': """
        Manage books.
    """,
    'description': """
       Module with Odoo basic concepts
    """,
    'author': "Maria Fernanda",

    'category': 'Uncategorized',
    'version': '15.0.1.0.0',

    'depends': ['base', 'website'],

    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/author_views.xml',
        'views/partner_view.xml',
        'views/templates.xml',
        'report/report_actions.xml',
        'report/book_report_templates.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}