from odoo import models, fields

class CycleStatus(models.Model):
    _name = 'mootiv.cycle_status'
    _description = 'Cycle Status'

    name = fields.Selection(
        [
            ('draft', 'Draft'),
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('canceled', 'Canceled'),
            ('completed', 'Completed')
        ],
        string='Status',
        required=True
    )
