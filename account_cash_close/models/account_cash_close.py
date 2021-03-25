# Copyright 2020 Calyx S.A.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _
from datetime import datetime, timedelta

class AccountCashClose(models.Model):
    _name = "account.cash.close"
    _inherit = 'mail.thread'
    _rec_name = "name"

    name = fields.Char(string="Name", track_visibility="onchange")
    date = fields.Date(string="Date", track_visibility="onchange", default=fields.Date.today)
    manager_cash_open = fields.Float(string="Manager Cash Open", track_visibility="onchange", compute='get_yesterday_cash')
    cash_sales = fields.Float(string="Cash Sales", track_visibility="onchange")
    cash_credit_notes = fields.Float(string="Cash Credit Notes", track_visibility="onchange")
    cash_sales_pedido_ya = fields.Float(string="Cash Sales Pedido Ya", track_visibility="onchange")
    cash_credit_notes_pedido_ya = fields.Float(string="Cash Credit Notes Pedido Ya", track_visibility="onchange")
    cash_sales_rappi = fields.Float(string="Cash Sales Rappi", track_visibility="onchange")
    cash_credit_notes_rappi = fields.Float(string="Cash Credit Notes Rappi", track_visibility="onchange")
    sales_other_mostaza = fields.Float(string="Sales Other Mostaza", track_visibility="onchange")
    
    credit_card_sales = fields.Float(string="Credit Card Sales", track_visibility="onchange")
    credit_notes_credit_card = fields.Float(string="Credit Notes Credit Card", track_visibility="onchange")
    credit_card_sales_pedido_ya = fields.Float(string="Credit Card Sales Pedido Ya", track_visibility="onchange")
    credit_notes_pedido_ya = fields.Float(string="Credit Notes Pedido Ya", track_visibility="onchange")
    credit_card_sales_mercado_pago = fields.Float(string="Credit Card Sales Mercado Pago", track_visibility="onchange")
    credit_notes_mercado_pago = fields.Float(string="Credit Notes Mercado Pago", track_visibility="onchange")
    credit_card_sales_rappi = fields.Float(string="Credit Card Sales Rappi", track_visibility="onchange")
    credit_notes_rappi = fields.Float(string="Credit Notes Rappi", track_visibility="onchange")

    number_envelopes_mailbox = fields.Integer(string="Number Of Envelopes to the Mailbox", track_visibility="onchange")
    deposit_mailbox_safe = fields.Float(string="Deposit Mailbox Safe", track_visibility="onchange")
    other_income_expenses = fields.Float(string="Other Income / Expenses", track_visibility="onchange")
    vendor_payment_cash = fields.Float(string="Vendor Payment in Cash", track_visibility="onchange")
    closing_cash_manager = fields.Float(string="Closing Cash Manager", track_visibility="onchange")
    
    manager_cash_difference = fields.Float(string="Manager Cash Difference", track_visibility="onchange", compute='set_manager_cash_difference')

    other_income_expenses_lines = fields.One2many('account.income.expenses','income_expenses_id')
    transfers_liniers_lines = fields.One2many('account.transfers.liniers','transfers_liniers_id')
    purchases_sales_lines = fields.One2many('account.purchases.sales','purchases_sales_id')
    
    @api.depends("manager_cash_open")
    def get_yesterday_cash(self):
        for rec in self:
            record = self.env['account.cash.close'].search([('date', '<', rec.date)], order='date desc', limit=1)
            if record:
                rec.manager_cash_open = record.closing_cash_manager
            else:
                rec.manager_cash_open = 0

    @api.depends("manager_cash_difference")
    def set_manager_cash_difference(self):
        for rec in self:
            total_positive = sum([rec.manager_cash_open,
                    rec.cash_sales,
                    rec.cash_sales_pedido_ya,
                    rec.cash_sales_rappi,
                    rec.sales_other_mostaza,
                    rec.other_income_expenses,
                    rec.vendor_payment_cash,
                    ])
            total_negative = sum([rec.closing_cash_manager,
                    rec.cash_credit_notes_rappi,
                    rec.cash_credit_notes_pedido_ya,
                    rec.cash_credit_notes,
                    rec.deposit_mailbox_safe,
                    ])
            rec.manager_cash_difference = total_positive - total_negative
    
    @api.onchange('date')
    def onchange_date(self):
        if self.date:
            self.name = "Caja " + self.date.replace('-','/')


    @api.onchange('purchases_sales_lines')
    def onchange_purchases_sales_lines(self):
        total = 0
        if self.purchases_sales_lines:
            for line in self.purchases_sales_lines:
                total += line.income - line.expenses
            self.sales_other_mostaza = total

    @api.onchange('other_income_expenses_lines')
    def onchange_other_income_expenses_lines(self):
        total = 0
        if self.other_income_expenses_lines:
            for line in self.other_income_expenses_lines:
                total += line.income - line.expenses
            self.other_income_expenses = total

    _sql_constraints = [
        ("cash_uniq","unique(date)",
        _("You only can have one cash per day")),
        ('cash_credit_notes_negative', 'CHECK(1=1)',
         _('Credit Notes must be negative!')),
        ('cash_credit_notes_pedido_ya_negative', 'CHECK(1=1)',
         _('Credit Notes (Pedido Ya) must be negative!')),
        ('cash_credit_notes_rappi_negative', 'CHECK(1=1)',
         _('Credit Notes (Rappi) must be negative!')),
        ('credit_notes_credit_card_negative', 'CHECK(1=1)',
         _('Credit Card Credit Notes must be negative!')),
        ('credit_notes_pedido_ya_negative', 'CHECK(1=1)',
         _('Credit Card Credit Notes (Pedido Ya) must be negative!')),
        ('credit_notes_mercado_pago_negative', 'CHECK(1=1)',
         _('Credit Card Credit Notes (Mercado Pago) must be negative!')),
        ('credit_notes_rappi_negative', 'CHECK(1=1)',
         _('Credit Card Credit Notes (Rappi) must be negative!')),
        ('cash_sales_positive', 'CHECK(cash_sales >= 0)',
         _('Cash Sales  must be positive!')),
        ('cash_sales_pedido_ya_positive', 'CHECK(cash_sales_pedido_ya >= 0)',
         _('Cash Sales (Pedido Ya) must be positive!')),
        ('cash_sales_rappi_positive', 'CHECK(cash_sales_rappi >= 0)',
         _('Cash Sales (Rappi) must be positive!')),
        ('credit_card_sales_positive', 'CHECK(credit_card_sales >= 0)',
         _('Credit Cards Sales  must be positive!')),
        ('credit_card_sales_pedido_ya_positive', 'CHECK(credit_card_sales_pedido_ya >= 0)',
         _('Credit Cards Sales (Pedido Ya) must be positive!')),
        ('credit_card_sales_mercado_pago_positive', 'CHECK(credit_card_sales_mercado_pago >= 0)',
         _('Credit Cards Sales (Mercado Pago) must be positive!')),
        ('credit_card_sales_rappi_positive', 'CHECK(credit_card_sales_rappi >= 0)',
         _('Credit Cards Sales (Rappi) must be positive!')),
    ]