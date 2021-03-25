# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Cash Close from Account',
    'summary': """
        this module allows to close a cash from account like Pos""",
    'author': 'Calyx Servicios S.A.',
    'maintainers': ['Paradiso'],
    'website': 'http://odoo.calyx-cloud.com.ar/',
    'license': 'AGPL-3',
    'category': 'Accounting',
    'version': '11.0.1.0.0',
    'development_status': 'Production/Stable',
    'application': False,
    'installable': True,
    'depends': ['mail','analytic'],
    'data': [
        'views/assets.xml',
        'views/account_cash_close_views.xml',
    ],
}
