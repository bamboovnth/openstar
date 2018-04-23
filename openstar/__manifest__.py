# -*- coding: utf-8 -*-
{
    'name': "Open Star",

    'summary': """
        first module""",

    'description': """
        first module in home odoo
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report', 'board'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openstar.xml',
        'views/partner.xml',
        'views/session_workflow.xml',
        'openstarupdate/openstar_app_view.xml',
        'security/security.xml',
        'views/user.xml',
        'report.xml',
        'views/session_board.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
