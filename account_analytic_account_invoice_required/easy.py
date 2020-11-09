from odoo import models, api, fields, _
from odoo.exceptions import UserError, ValidationError

class EasyInvoice(models.Model):
    _inherit = "easy.invoice"

    @api.multi
    def confirm(self):
        for eas in self:
            for rec in eas.invoice_line_ids:
                if not rec.analytic_account_id.id:
                    raise ValidationError(_('Analytic account must be defined '))
        res = super(EasyInvoice, self).confirm()
        return res 

class EasyInvoiceLine(models.Model):
    _inherit = "easy.invoice.line"

    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account', required=True)