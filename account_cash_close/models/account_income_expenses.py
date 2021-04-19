from odoo import api, fields, models, _, exceptions

class AccountIncomeExpenses(models.Model):
    _name = 'account.income.expenses'
    _description = 'Income/Expenses'

    @api.model
    def _filter_accounts(self):
        account = []
        get_cashbox_account = self.env['account.account.cashbox'].search([])
        if get_cashbox_account.other_income_expenses_accounts:
            for rec in get_cashbox_account.other_income_expenses_accounts:
                account.append(rec.id)
            return [('id', 'in', account)]

    income_expenses_id = fields.Many2one('account.cash.close', string='Income/Expenses')
    details = fields.Char(string="Details")
    income = fields.Float(string="Income")
    expenses = fields.Float(string="Expenses")
    other_income_expenses_account = fields.Many2one('account.account', string="Account", domain=_filter_accounts)
