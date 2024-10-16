import json
import math
from urllib.parse import parse_qs

from odoo import http
from odoo.http import request


def valid_response(data,pagination_info,status_code):
    respose_body={
        'message':"successfully fetched api",
        'data':data
    }
    if pagination_info:
        respose_body['pagination_info']=pagination_info
    return request.make_json_response(respose_body, status=status_code)

class CourseApi(http.Controller):
    @http.route("/v1/course",methods=["POST"],type="http",auth="none",csrf=False)
    def post_course(self):
        args=request.httprequest.data.decode()
        vals=json.loads(args)
        print("inside post test point",vals)
        res=request.env['course.management'].sudo().create(vals)
        print(res)
        if res:
            return valid_response({
                "message":"done post"
            },{},200)



    @http.route("/v1/course/json/<int:course_id>", methods=["PUT"], type="json", auth="none", csrf=False)
    def update_property_json(self,course_id):
        try:
            course_id=request.env['course.management'].sudo().search([
                ("id","=",course_id)
            ])
            if not course_id:
                return {
                    "message": "id not found",
                }
            print(course_id)
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            print(vals)
            course_id.write(vals)
            return valid_response({
                "message": "updated successfully",
                "id":course_id.id,
            },{},201)

        except Exception as error:
            return {
                    "message": error,
                }

    @http.route("/v1/get_range_courses/json", methods=["GET"], type="http", auth="none", csrf=False)
    def get_courses_json(self, instructor_id=None, start_date=None, end_date=None, **kwargs):
        print("asd")
        try:
            domain = []
            if instructor_id:
                domain.append(('instructor_id', '=', int(instructor_id)))

            if start_date and end_date:
                domain.append(('lesson_ids.date', '>=', start_date))
                domain.append(('lesson_ids.date', '<=', end_date))

            courses = request.env['course.management'].sudo().search(domain)

            course_data = []
            for course in courses:
                course_data.append({
                    'name': course.name,
                    'instructor': course.instructor_id.name,
                    'room': course.room_id.name,
                    'number_of_lessons': len(course.lesson_ids),
                })

            return request.make_json_response({
                'status': 'success',
                'courses': course_data
            })


        except Exception as e:

            return request.make_json_response({'status': 'error', 'message': str(e)}, status=500)


