from odoo import models, fields

class Trainer(models.Model):
    _name = 'mootiv.trainer'
    _description = 'Trainer'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    dni = fields.Char(string='DNI', required=True, help='DNI of the trainer')
    name = fields.Char(string='First Name', required=True, tracking=True, help='First name of the trainer')
    last_name = fields.Char(string='Last Name', required=True, tracking=True, help='Last name of the trainer')
    email = fields.Char(string='Email', help='Email address of the trainer')
    telephone = fields.Char(string='Telephone', help='Telephone number of the trainer')
    birthdate = fields.Date(string='Birthdate', help='Birthdate of the trainer')
    active = fields.Boolean(string='Is Active', default=True, help='Indicates if the trainer is active')
    students_ids = fields.One2many(
        'mootiv.student',
        'trainer_id',
        string='Students',
        help='Students assigned to the trainer'
    )
    age = fields.Integer(
        string='Age',
        compute='_compute_age',
        store=True,
        help='Age of the trainer'
    )

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
