from odoo import models, fields, api
from datetime import date

class TrainingPlan(models.Model):
    _name = 'mootiv.training_plan'
    _description = 'Training Plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    student_id = fields.Many2one(
        'res.partner',
        string='Student',
        required=True,
        ondelete='cascade',
        help='Student associated with this training plan'
    )
    training_cycles_ids = fields.One2many(
        'mootiv.training_cycle',
        'training_plan_id',
        string='Training Cycles',
        help='List of training cycles in this plan'
    )

    def create_new_cycle(self, start_date, number_of_weeks, number_of_days, goal_id, training_type_id):
        """Create a new training cycle."""
        if not self.training_cycles_ids:
            self.training_cycles_ids = []

        # Validate that the start date is not in the past
        if start_date < date.today():
            raise ValueError("The start date of the cycle cannot be in the past.")

        # Validate overlap with existing cycles
        for cycle in self.training_cycles_ids:
            if not cycle.is_canceled and cycle.overlaps_with(start_date, number_of_weeks):
                raise ValueError("The new cycle overlaps with an existing active cycle.")

        # Create a new cycle
        new_cycle = self.env['mootiv.training_cycle'].create({
            'start_date': start_date,
            'goal_id': goal_id,
            'training_type_id': training_type_id,
            'status': 'draft',
            'days_of_training': number_of_days,
        })
        self.training_cycles_ids = [(4, new_cycle.id)]
