from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Room(models.Model):
    _name = 'room.management'
    _description='Room'

    name = fields.Char(string='Room Name', required=True)
    capacity=fields.Integer(required=True)
    lesson_ids = fields.One2many('lesson.management', 'room_id', string='Lessons')
