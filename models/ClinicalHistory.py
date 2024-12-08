from odoo import models, fields

class ClinicalHistory(models.Model):
    _name = 'mootiv.clinical_history'
    _description = 'Clinical History'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    condition_ids = fields.One2many(
        'mootiv.condition',
        'clinical_history_id',
        string='Conditions',
        help='Conditions associated with this clinical history'
    )

    def add_condition(self, condition_vals):
        """ Add a condition to the clinical history """
        self.ensure_one()
        self.env['mootiv.condition'].create({**condition_vals, 'clinical_history_id': self.id})

    def remove_condition(self, condition_id):
        """ Remove a condition by its ID """
        condition = self.env['mootiv.condition'].browse(condition_id)
        if condition and condition.clinical_history_id.id == self.id:
            condition.unlink()
        else:
            raise ValueError('Condition not found or does not belong to this clinical history')
