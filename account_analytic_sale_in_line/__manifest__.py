# -*- encoding: utf-8 -*-

{
    'name': 'Account Analitic in line of  Sale Order',
    'version': '11.0.1.0.0',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Traspasa a las lineas del Sale Order la cuenta analitica',
    'description': """
Account Analityc Required
=========================

    """,
    'author': 'Calyx',
    'website': 'http://www.calyxservicios.com.ar',
    'depends': ['account', 'sale'],

    'data': [
        'views/sale_order_view.xml'
    ],

    'installable': True,
    'active': False,
}
