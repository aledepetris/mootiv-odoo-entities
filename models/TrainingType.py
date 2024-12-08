from odoo import models, fields

class TrainingType(models.Model):
    _name = 'mootiv.training_type'
    _description = 'Training Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(string='Name', required=True, tracking=True, help='Name of the training type')
    description = fields.Text(string='Description', help='Description of the training type')
    exercise_types_ids = fields.Many2many(
        'mootiv.exercise_type',
        'training_type_exercise_type_rel',
        'training_type_id',
        'exercise_type_id',
        string='Exercise Types',
        help='Exercise types associated with this training type'
    )
