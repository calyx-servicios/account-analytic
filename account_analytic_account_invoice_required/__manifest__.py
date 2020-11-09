# -*- encoding: utf-8 -*-

{
    'name': 'Account Analitic Account Invoice Required',
    'version': '0.1',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Transforma en requerido el campo de cuenta analitica en facturas',
    'description': """
Account Analityc Required
=========================

    """,
    'author': 'Calyx',
    'website': 'http://www.calyxservicios.com.ar',
    'depends': [
        'account',
        'base', 
        'easy_invoice',
        'easy_invoice_partner_cc',
        'easy_invoice_employee_expense',
        'easy_invoice_employee_cc',
        'easy_invoice_sale',
        'account_analytic_sale_in_line',
    ],
    'data': [],
    'installable': True,
    'active': False,
}
