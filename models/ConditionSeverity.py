from odoo import models, fields

class ConditionSeverity(models.Model):
    _name = 'mootiv.condition_severity'
    _description = 'Condition Severity'

    severity = fields.Selection(
        [
            ('low', 'Low'),
            ('moderate', 'Moderate'),
            ('severe', 'Severe')
        ],
        string='Condition Severity',
        required=True,
        help='Severity level of the condition'
    )
