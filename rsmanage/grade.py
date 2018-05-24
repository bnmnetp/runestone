from rs_grading import do_autograde, do_calculate_totals
import json, datetime, sys

userinfo = json.loads(os.environ['RSM_USERINFO'])
# print(userinfo['course'], userinfo['pset'])
# # print(db.keys())
# print(settings)

assignmentid = userinfo['pset']
assignment = db(db.assignments.id == assignmentid).select().first()
course=db(db.courses.course_name == userinfo['course']).select().first()
do_autograde(assignment,
             course.id,
             course.course_name,
             sid = None,
             question_name = None,
             enforce_deadline = userinfo['enforce_deadline'],
             timezoneoffset = 5,
             db=db,
             settings=settings)

do_calculate_totals(assignment,
                    course.id,
                    course.course_name,
                    sid = None,
                    db = db,
                    settings = settings)