# -*- coding: utf-8 -*-
{
    'name': "Paystack",

    'summary': """
        This is the paystack module for Odoo using Javascript""",

    'description': """
        Paystack
    """,

    'author': "Tijesunimi Peters",
    'website': "https://github.com/andela-tpeters",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'payment',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/paystack.xml'
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}