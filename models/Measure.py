from odoo import models, fields, api

class Measure(models.Model):
    _name = 'mootiv.measure'
    _description = 'Measure'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id = fields.Integer(string='ID', readonly=True)
    date = fields.Date(string='Date', required=True, help='Date of the measurement')
    height = fields.Float(string='Height (m)', help='Height in meters')
    weight = fields.Float(string='Weight (kg)', help='Weight in kilograms')
    shoulder = fields.Float(string='Shoulder Circumference (cm)', help='Measurement of shoulder circumference')
    chest = fields.Float(string='Chest Circumference (cm)', help='Measurement of chest circumference')
    arm = fields.Float(string='Arm Circumference (cm)', help='Measurement of arm circumference')
    waist = fields.Float(string='Waist Circumference (cm)', help='Measurement of waist circumference')
    hip = fields.Float(string='Hip Circumference (cm)', help='Measurement of hip circumference')
    leg = fields.Float(string='Leg Circumference (cm)', help='Measurement of leg circumference')
    bmi = fields.Float(string='Body Mass Index (BMI)', compute='_compute_bmi', store=True)
    waist_to_hip_ratio = fields.Float(string='Waist-to-Hip Ratio', compute='_compute_waist_to_hip_ratio', store=True)
    waist_to_height_ratio = fields.Float(string='Waist-to-Height Ratio', compute='_compute_waist_to_height_ratio', store=True)
    bmi_category = fields.Selection(
        [
            ('underweight', 'Underweight'),
            ('normal', 'Normal'),
            ('overweight', 'Overweight'),
            ('obesity', 'Obesity')
        ],
        string='BMI Category',
        compute='_compute_bmi_category',
        store=True
    )

    @api.depends('height', 'weight')
    def _compute_bmi(self):
        for record in self:
            if record.height and record.height > 0 and record.weight:
                record.bmi = record.weight / (record.height * record.height)
            else:
                record.bmi = 0.0

    @api.depends('waist', 'hip')
    def _compute_waist_to_hip_ratio(self):
        for record in self:
            if record.hip and record.hip > 0:
                record.waist_to_hip_ratio = record.waist / record.hip
            else:
                record.waist_to_hip_ratio = 0.0

    @api.depends('waist', 'height')
    def _compute_waist_to_height_ratio(self):
        for record in self:
            if record.height and record.height > 0:
                record.waist_to_height_ratio = record.waist / (record.height * 100)
            else:
                record.waist_to_height_ratio = 0.0

    @api.depends('bmi')
    def _compute_bmi_category(self):
        for record in self:
            if record.bmi < 18.5:
                record.bmi_category = 'underweight'
            elif record.bmi < 25:
                record.bmi_category = 'normal'
            elif record.bmi < 30:
                record.bmi_category = 'overweight'
            else:
                record.bmi_category = 'obesity'
