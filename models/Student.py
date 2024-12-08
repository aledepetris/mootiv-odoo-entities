from odoo import models, fields, api

class Student(models.Model):
    _name = 'mootiv.student'
    _description = 'Student'
    _inherit = ['mootiv.person', 'mail.thread', 'mail.activity.mixin']

    start_date = fields.Date(string='Start Date', tracking=True)
    trainer_id = fields.Many2one('mootiv.trainer', string='Trainer', ondelete='set null')
    training_plan_id = fields.Many2one('mootiv.training_plan', string='Training Plan', ondelete='set null')
    clinical_history_id = fields.Many2one('mootiv.clinical_history', string='Clinical History', ondelete='cascade')
    measure_ids = fields.One2many('mootiv.measure', 'student_id', string='Measures')
    training_place_ids = fields.One2many('mootiv.training_place', 'student_id', string='Training Places')

    @api.depends('birthdate')
    def _compute_age(self):
        super(Student, self)._compute_age()

    @api.model
    def create(self, vals):
        """ Add custom logic for student creation if necessary """
        return super(Student, self).create(vals)
