from odoo import api, fields, models, _, exceptions

class AccountTransfersLiniers(models.Model):
    _name = 'account.transfers.liniers'
    _description = 'Transfers to Liniers'

    transfers_liniers_id = fields.Many2one('account.cash.close', string='Transfers to Liniers')
    details = fields.Char(string="Details")
    income = fields.Float(string="Income")
    expenses = fields.Float(string="Expenses")