from odoo import models, fields

class ExerciseRoutine(models.Model):
    _name = 'mootiv.exercise_routine'
    _description = 'Exercise Routine'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    exercise_id = fields.Many2one(
        'mootiv.exercise',
        string='Exercise',
        required=True,
        ondelete='cascade',
        help='The exercise associated with this routine'
    )
    sets = fields.Integer(string='Sets', help='Number of sets for the exercise')
    repetitions = fields.Integer(string='Repetitions', help='Number of repetitions per set')
    weight = fields.Float(string='Weight (kg)', help='Weight used for the exercise')
    rest = fields.Integer(string='Rest (seconds)', help='Rest time between sets in seconds')
    notes = fields.Text(string='Notes', help='Additional notes about the routine')
