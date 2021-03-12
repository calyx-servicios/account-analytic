from odoo import api, fields, models, _, exceptions

class AccountPurchaseSales(models.Model):
    _name = 'account.purchases.sales'
    _description = 'Others Mostaza Purchases and Sales'

    purchases_sales_id = fields.Many2one('account.cash.close', string='Others Mostaza Purchases and Sales')
    details = fields.Char(string="Details")
    income = fields.Float(string="Income")
    expenses = fields.Float(string="Expenses")