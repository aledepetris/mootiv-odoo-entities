from odoo import models, fields

class TrainingWeek(models.Model):
    _name = 'mootiv.training_week'
    _description = 'Training Week'

    name = fields.Char(string='Week Name', required=True, help='Name of the training week')
    status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('postponed', 'Postponed'),
            ('canceled', 'Canceled'),
            ('completed', 'Completed')
        ],
        string='Week Status',
        required=True,
        default='draft',
        help='The current status of the training week'
    )
