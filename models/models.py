# -*- coding: utf-8 -*-

from odoo import models, fields, api

class payment_paystack(models.Model):
    _name = 'payment_paystack.payment_paystack'

    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100

class Payment(models.Model):
    _name = 'payment_paystack.payment'

    name = fields.Char()
    description = fields.Text()