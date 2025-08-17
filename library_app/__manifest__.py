# -*- coding: utf-8 -*-
{
    'name': 'Library App',
    'version': '1.0',
    'summary': 'A simple app using an external Python library',
    'description': """
        This app demonstrates how to use an external Python library (requests) in an Odoo.sh environment.
    """,
    'author': 'Mafer Morales',
    'website': 'https://www.yourwebsite.com',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'views/library_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}