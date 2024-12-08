from odoo import models, fields

class Equipment(models.Model):
    _name = 'mootiv.equipment'
    _description = 'Equipment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(string='Name', required=True, tracking=True, help='Name of the equipment')
