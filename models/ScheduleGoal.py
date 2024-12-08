from odoo import models, fields

class ScheduleGoal(models.Model):
    _name = 'mootiv.schedule_goal'
    _description = 'Schedule Goal'

    id = fields.Integer(string='ID', readonly=True)
    day_of_training = fields.Integer(string='Day of Training', required=True)
    training_types_ids = fields.Many2many(
        'mootiv.training_type',
        'schedule_goal_training_type_rel',
        'schedule_goal_id',
        'training_type_id',
        string='Training Types',
        help='Training types associated with this schedule goal'
    )
    goal_id = fields.Many2one(
        'mootiv.goal',
        string='Goal',
        ondelete='cascade',
        help='The goal this schedule is associated with'
    )
