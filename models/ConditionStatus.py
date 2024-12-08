from odoo import models, fields

class ConditionStatus(models.Model):
    _name = 'mootiv.condition_status'
    _description = 'Condition Status'

    status = fields.Selection(
        [
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('resolved', 'Resolved')
        ],
        string='Condition Status',
        required=True
    )
