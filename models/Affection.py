from odoo import models, fields

class Affection(models.Model):
    _name = 'mootiv.affection'
    _description = 'Affection'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    muscles_affected_ids = fields.Many2many(
        'mootiv.muscle',
        string='Muscles Affected',
        help='Muscles affected by this condition'
    )
