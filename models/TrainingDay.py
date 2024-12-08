from odoo import models, fields, api

class TrainingDay(models.Model):
    _name = 'mootiv.training_day'
    _description = 'Training Day'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    finish_date = fields.Date(string='Finish Date', help='The date when the training day was completed')
    exercises_ids = fields.One2many(
        'mootiv.exercise_routine',
        'training_day_id',
        string='Exercises',
        help='List of exercises for this training day'
    )
    is_completed = fields.Boolean(
        string='Is Completed',
        compute='_compute_is_completed',
        store=True,
        help='Indicates if the training day is completed'
    )

    @api.depends('finish_date')
    def _compute_is_completed(self):
        for record in self:
            record.is_completed = record.finish_date is not None
