from odoo import models, fields

class TrainingPlace(models.Model):
    _name = 'mootiv.training_place'
    _description = 'Training Place'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(string='Name', required=True, tracking=True, help='Name of the training place')
    equipment_ids = fields.Many2many(
        'mootiv.equipment',
        'training_place_equipment_rel',
        'training_place_id',
        'equipment_id',
        string='Equipments',
        help='Equipments available at this training place'
    )
