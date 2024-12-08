from odoo import models, fields

class Exercise(models.Model):
    _name = 'mootiv.exercise'
    _description = 'Exercise'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(string='Name', required=True, tracking=True, help='Name of the exercise')
    description = fields.Text(string='Description', help='Description of the exercise')
    is_for_time = fields.Boolean(string='Is For Time', help='Indicates if the exercise is time-based')
    is_total = fields.Boolean(string='Is Total', help='Indicates if the exercise is a total body exercise')
    muscles_ids = fields.Many2many(
        'mootiv.muscle',
        'exercise_muscle_rel',
        'exercise_id',
        'muscle_id',
        string='Muscles',
        help='Muscles targeted by this exercise'
    )
    exercise_types_ids = fields.Many2many(
        'mootiv.exercise_type',
        'exercise_type_rel',
        'exercise_id',
        'exercise_type_id',
        string='Exercise Types',
        help='Types of this exercise'
    )
    equipment_ids = fields.Many2many(
        'mootiv.equipment',
        'exercise_equipment_rel',
        'exercise_id',
        'equipment_id',
        string='Equipment',
        help='Equipment required for this exercise'
    )
