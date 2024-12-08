from odoo import models, fields, api

class Muscle(models.Model):
    _name = 'mootiv.muscle'
    _description = 'Muscle'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(string='Name', required=True, tracking=True)
    type = fields.Selection(
        [('single', 'Single Muscle'), ('group', 'Muscle Group')],
        string='Type',
        required=True,
        default='single'
    )
    exercises_ids = fields.Many2many(
        'mootiv.exercise',
        string='Exercises Associated',
        help='Exercises that target this muscle'
    )
    associated_muscles_ids = fields.Many2many(
        'mootiv.muscle',
        'muscle_group_rel',
        'parent_muscle_id',
        'child_muscle_id',
        string='Associated Muscles',
        help='Muscles that form part of this muscle group'
    )

    @api.depends('type')
    def is_a_muscle_group(self):
        for record in self:
            record.is_muscle_group = record.type == 'group'

    is_muscle_group = fields.Boolean(
        string='Is a Muscle Group',
        compute='is_a_muscle_group',
        store=True
    )
