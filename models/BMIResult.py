from odoo import models, fields

class BMIResult(models.Model):
    _name = 'mootiv.bmi_result'
    _description = 'BMI Result'

    result = fields.Selection(
        [
            ('underweight', 'Underweight'),
            ('normal', 'Normal'),
            ('overweight', 'Overweight'),
            ('obesity', 'Obesity')
        ],
        string='Result',
        required=True
    )
