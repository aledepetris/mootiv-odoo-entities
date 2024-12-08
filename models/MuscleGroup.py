from odoo import models, fields, api

class MuscleGroup(models.Model):
    _inherit = 'mootiv.muscle'

    muscles_ids = fields.Many2many(
        'mootiv.muscle',
        'muscle_group_rel',
        'group_id',
        'muscle_id',
        string='Associated Muscles',
        help='Muscles that are part of this muscle group',
        domain=[('type', '=', 'single')]
    )

    @api.model
    def create(self, vals):
        vals['type'] = 'group'
        return super(MuscleGroup, self).create(vals)

    def write(self, vals):
        vals['type'] = 'group'
        return super(MuscleGroup, self).write(vals)
