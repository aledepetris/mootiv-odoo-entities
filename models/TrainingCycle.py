from odoo import models, fields, api
from datetime import timedelta

class TrainingCycle(models.Model):
    _name = 'mootiv.training_cycle'
    _description = 'Training Cycle'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    start_date = fields.Date(string='Start Date', required=True, help='Start date of the training cycle')
    weeks_ids = fields.One2many(
        'mootiv.training_week',
        'training_cycle_id',
        string='Training Weeks',
        help='List of training weeks in this cycle'
    )
    goal_id = fields.Many2one(
        'mootiv.goal',
        string='Goal',
        required=True,
        ondelete='cascade',
        help='Goal associated with this training cycle'
    )
    training_type_id = fields.Many2one(
        'mootiv.training_type',
        string='Training Type',
        required=True,
        ondelete='cascade',
        help='Training type for this cycle'
    )
    status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('canceled', 'Canceled'),
            ('completed', 'Completed')
        ],
        string='Cycle Status',
        required=True,
        default='draft',
        help='Current status of the training cycle'
    )
    days_of_training = fields.Integer(string='Days of Training', required=True, help='Number of training days per week')
    number_of_weeks = fields.Integer(string='Number of Weeks', compute='_compute_number_of_weeks', store=True)

    @api.depends('weeks_ids')
    def _compute_number_of_weeks(self):
        for record in self:
            record.number_of_weeks = len(record.weeks_ids)

    def change_status(self, new_status):
        valid_transitions = {
            'draft': ['pending'],
            'pending': ['in_progress'],
            'in_progress': ['completed', 'canceled'],
            'canceled': [],
            'completed': []
        }
        if new_status not in valid_transitions.get(self.status, []):
            raise ValueError(f"Cannot change status from {self.status} to {new_status}")
        self.status = new_status

    def create_weeks(self, number_of_weeks):
        """ Create training weeks for this cycle """
        if not self.start_date or not self.days_of_training:
            raise ValueError("Start date and days of training must be set")
        self.weeks_ids = [(5, 0, 0)]  # Clear existing weeks
        weeks = []
        for i in range(number_of_weeks):
            week_start_date = self.start_date + timedelta(weeks=i)
            week = self.env['mootiv.training_week'].create({
                'start_date': week_start_date,
                'status': 'draft',
                'days_of_training': self.days_of_training
            })
            weeks.append(week.id)
        self.weeks_ids = [(6, 0, weeks)]
