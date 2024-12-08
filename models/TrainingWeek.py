from odoo import models, fields, api

class TrainingWeek(models.Model):
    _name = 'mootiv.training_week'
    _description = 'Training Week'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    start_date = fields.Date(string='Start Date', required=True, help='Start date of the training week')
    days_ids = fields.One2many(
        'mootiv.training_day',
        'training_week_id',
        string='Training Days',
        help='List of training days in this week'
    )
    status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('postponed', 'Postponed'),
            ('canceled', 'Canceled'),
            ('completed', 'Completed')
        ],
        string='Status',
        required=True,
        default='draft',
        help='Current status of the training week'
    )
    progress = fields.Float(
        string='Progress (%)',
        compute='_compute_progress',
        store=True,
        help='Progress of the training week based on completed training days'
    )
    is_completed = fields.Boolean(
        string='Is Completed',
        compute='_compute_is_completed',
        store=True,
        help='Indicates if the training week is completed'
    )
    final_state = fields.Boolean(
        string='Is in Final State',
        compute='_compute_is_in_final_state',
        store=True,
        help='Indicates if the training week is in a final state'
    )

    @api.depends('days_ids.is_completed')
    def _compute_progress(self):
        for record in self:
            total_days = len(record.days_ids)
            if total_days > 0:
                completed_days = sum(1 for day in record.days_ids if day.is_completed)
                record.progress = (completed_days / total_days) * 100
            else:
                record.progress = 0.0

    @api.depends('days_ids.is_completed')
    def _compute_is_completed(self):
        for record in self:
            record.is_completed = all(day.is_completed for day in record.days_ids)

    @api.depends('status')
    def _compute_is_in_final_state(self):
        for record in self:
            record.final_state = record.status in ['completed', 'postponed']

    def change_status(self, new_status):
        if new_status not in ['draft', 'pending', 'in_progress', 'postponed', 'canceled', 'completed']:
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status
