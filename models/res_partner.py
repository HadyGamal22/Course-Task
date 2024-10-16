from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    course_ids = fields.One2many('course.management', 'instructor_id', string='Courses')
    instructor_ids = fields.Many2many(
        'res.partner',  # Related model
        'partner_instructor_rel',  # Relation table name
        'partner_id',  # Column for this model (res.partner)
        'instructor_partner_id',  # Column for related model (res.partner)
        string='Instructor Name'
    )
    @api.constrains('instructor_course_ids', 'attendee_course_ids')
    def _check_instructor_attendee(self):
        for partner in self:
            for course in partner.course_ids:
                if course in partner.instructor_ids:
                    raise ValidationError("A person cannot be both an instructor and an attendee of the same course.")
