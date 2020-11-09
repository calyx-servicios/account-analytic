# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, fields, _
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
            
    analytic_account_id = fields.Many2one('account.analytic.account', 'Account Analytic')
   
    @api.multi
    def _prepare_invoice_line(self, qty):
    	res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
    	if 'account_analytic_id' in res:
    		res['account_analytic_id'] = self.analytic_account_id.id
    	return res
       
