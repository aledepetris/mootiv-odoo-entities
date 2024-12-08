from odoo import models, fields, api

class Goal(models.Model):
    _name = 'mootiv.goal'
    _description = 'Goal'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    schedule_goals_ids = fields.One2many(
        'mootiv.schedule_goal',
        'goal_id',
        string='Schedule Goals',
        help='Schedules associated with this goal'
    )

    def get_training_types_by_days_of_training(self, days):
        """ Retrieve training types based on days of training """
        self.ensure_one()
        schedule_goal = self.schedule_goals_ids.filtered(lambda sg: sg.day_of_training == days)
        return schedule_goal.mapped('training_types_ids')

    def get_days_of_training(self):
        """ Get list of days of training """
        self.ensure_one()
        return self.schedule_goals_ids.mapped('day_of_training')
