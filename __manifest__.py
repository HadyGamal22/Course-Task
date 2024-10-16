{
    'name': 'Course Task',
    'description': 'Task 13 oct 2024 ',
    'author': 'Hady Gamal',
    'depends': ['base','contacts','website'],
    'data':[
        'views/course_menu.xml',
        'views/course_template.xml',
        'views/base_menu.xml',
        'views/course_view.xml',
        'views/room_view.xml',
        'views/lesson_view.xml',
        'views/res_partner.xml',
        'reports/courses_report.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'course_task/static/src/courses_website.css',  # Path to your CSS
        ],
    }
}
