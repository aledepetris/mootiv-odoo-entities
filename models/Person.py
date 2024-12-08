from odoo import models, fields

class Person(models.Model):
    _name = 'mootiv.person'
    _description = 'Person'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    dni = fields.Char(string='DNI', required=True, tracking=True)
    name = fields.Char(string='First Name', required=True, tracking=True)
    last_name = fields.Char(string='Last Name', required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    telephone = fields.Char(string='Telephone')
    birthdate = fields.Date(string='Birthdate')
    active = fields.Boolean(string='Active', default=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                today = fields.Date.today()
                record.age = today.year - record.birthdate.year - (
                    (today.month, today.day) < (record.birthdate.month, record.birthdate.day)
                )
            else:
                record.age = 0
