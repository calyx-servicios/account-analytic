# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, fields, _

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    account_analytic_id = fields.Many2one('account.analytic.account', string='Analytic Account', required="True")
        