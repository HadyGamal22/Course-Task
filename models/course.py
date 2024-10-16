from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CourseManagement(models.Model):
    _name = 'course.management'
    _description='Course'

    name = fields.Char(required=True)
    instructor_id=fields.Many2one('res.partner',string='Instructor Name')
    room_id=fields.Many2one('room.management')
    attendee_ids = fields.Many2many('res.partner', string='Attendees')
    lesson_ids=fields.One2many('lesson.management','course_id',readonly=1)
    capacity = fields.Integer(related='room_id.capacity')
    description=fields.Char(required=True)
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_attendee_course(self):
        for rec in self:
            if rec.instructor_id and rec.instructor_id in rec.attendee_ids:
                raise ValidationError("A person cannot be both an instructor and an attendee for the same course.")

    @api.constrains('attendee_ids', 'capacity')
    def check_capacity(self):
        if len(self.attendee_ids) > self.capacity:
            raise ValidationError("The number of attendees exceeds the room capacity.")



    @api.onchange('room_id')
    def _onchange_measurements(self):
        if self.room_id:
            # Clear existing lines in measurement_ids
            self.lesson_ids = [(5, 0, 0)]

            # Get measurement lines from selected `measurements`
            new_lessons = self.room_id.lesson_ids
            print(new_lessons)
            # Populate measurement_ids with lines from the selected `measurements`
            lines = [(0, 0, {
                'name': line.name,
                'date': line.date,
            }) for line in new_lessons]
            self.lesson_ids = lines