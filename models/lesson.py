from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Lessons(models.Model):
    _name = 'lesson.management'
    _description = 'lessons'

    room_id=fields.Many2one('room.management')
    name = fields.Char(required=True)
    course_id = fields.Many2one('course.management', string='Course')
    date = fields.Datetime(string='Lesson Date')