from odoo import models, fields

class ExerciseType(models.Model):
    _name = 'mootiv.exercise_type'
    _description = 'Exercise Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(string='Name', required=True, tracking=True, help='Name of the exercise type')
