from odoo import api, fields, models, _, exceptions

class AccountAccountCashBox(models.Model):
    _name = 'account.account.cashbox'
    _description = 'Cashbox Accounts'

    cash_sales_account = fields.Many2one(string="Cash Sales", comodel_name='account.account')
    cash_credit_notes_account = fields.Many2one(string="Cash Credit Notes", comodel_name='account.account') 
    cash_sales_pedido_ya_account = fields.Many2one(string="Cash Sales Pedido Ya", comodel_name='account.account') 
    cash_credit_notes_pedido_ya_account = fields.Many2one(string="Cash Credit Notes Pedido Ya", comodel_name='account.account') 
    cash_sales_rappi_account = fields.Many2one(string="Cash Sales Rappi", comodel_name='account.account') 
    cash_credit_notes_rappi_account = fields.Many2one(string="Cash Credit Notes Rappi", comodel_name='account.account') 
    
    credit_card_sales_account = fields.Many2one(string="Credit Card Sales", comodel_name='account.account') 
    credit_notes_credit_card_account = fields.Many2one(string="Credit Notes Credit Card", comodel_name='account.account') 
    credit_card_sales_pedido_ya_account = fields.Many2one(string="Credit Card Sales Pedido Ya", comodel_name='account.account') 
    credit_notes_pedido_ya_account = fields.Many2one(string="Credit Notes Pedido Ya", comodel_name='account.account') 
    credit_card_sales_mercado_pago_account = fields.Many2one(string="Credit Card Sales Mercado Pago", comodel_name='account.account') 
    credit_notes_mercado_pago_account = fields.Many2one(string="Credit Notes Mercado Pago", comodel_name='account.account') 
    credit_card_sales_rappi_account = fields.Many2one(string="Credit Card Sales Rappi", comodel_name='account.account') 
    credit_notes_rappi_account = fields.Many2one(string="Credit Notes Rappi", comodel_name='account.account')