from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    course_ids = fields.One2many('course.management', 'instructor_id', string='Courses')
    instructor_ids = fields.Many2many(
        'res.partner',
        'partner_instructor_rel',
        'partner_id',
        'instructor_partner_id',
        string='Instructor Name'
    )

   