from odoo import api, fields, models, _, exceptions

class AccountIncomeExpenses(models.Model):
    _name = 'account.income.expenses'
    _description = 'Income/Expenses'

    income_expenses_id = fields.Many2one('account.cash.close', string='Income/Expenses')
    details = fields.Char(string="Details")
    income = fields.Float(string="Income")
    expenses = fields.Float(string="Expenses")