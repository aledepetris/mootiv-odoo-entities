from odoo import models, fields, api

class SingleMuscle(models.Model):
    _inherit = 'mootiv.muscle'

    @api.model
    def create(self, vals):
        vals['type'] = 'single'
        return super(SingleMuscle, self).create(vals)

    def write(self, vals):
        vals['type'] = 'single'
        return super(SingleMuscle, self).write(vals)
