from odoo import http
from odoo.http import request

class CourseController(http.Controller):
    @http.route('/courses', type='http', auth='public', website=True)
    def list_courses(self, **kwargs):
        courses = request.env['course.management'].search([])
        return request.render('course_task.courses_template', {'courses': courses})
