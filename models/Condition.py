from odoo import models, fields

class Condition(models.Model):
    _name = 'mootiv.condition'
    _description = 'Condition'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    affection_id = fields.Many2one(
        'mootiv.affection',
        string='Affection',
        ondelete='cascade',
        required=True
    )
    diagnosis_date = fields.Date(string='Diagnosis Date', required=True)
    severity = fields.Selection(
        [
            ('low', 'Low'),
            ('moderate', 'Moderate'),
            ('severe', 'Severe')
        ],
        string='Severity',
        required=True,
        help='Severity of the condition'
    )
    current_status = fields.Selection(
        [
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('resolved', 'Resolved')
        ],
        string='Current Status',
        required=True,
        help='Current status of the condition'
    )
    notes = fields.Text(string='Notes')
