#from invokes import invoke_http, all_route
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)

# Remember to add/remove the app config with your php password
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://root:@localhost:3306/is212_all_in_one'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)
#route_dict = all_route()
class Course(db.Model):
    tablename = 'Course'

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(32), nullable=False)
    course_desc = db.Column(db.String(32), nullable=False)
    course_status = db.Column(db.String(32), nullable=False)
    course_type = db.Column(db.String(32), nullable=False)
    course_category = db.Column(db.String(32), nullable=False)

    def __init__(self, course_id, course_name, course_desc, course_status, course_type, course_category):
        self.course_id = course_id
        self.course_name = course_name
        self.course_desc = course_desc
        self.course_status = course_status
        self.course_type = course_type
        self.course_category = course_category

    def json(self):
        dto = {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'course_desc': self.course_desc,
            'course_status': self.course_status,
            'course_type': self.course_type,
            'course_category': self.course_category,
        }
        return dto 

db.create_all()

#role_database = invoke_http(route_dict["role"] , method='GET')
@app.route("/course")
def course_get_all():
    course_list = Course.query.all()
    
    if course_list:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "courses": [course.json() for course in course_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Courses."
        }
    ), 404


@app.route("/course/name/<string:course_name>", methods=['GET'])
def get_course_by_name(course_name):
    course_data = Course.query.filter_by(course_name = course_name).first()
    if course_data:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "courses": course_data.json()
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": 'No course named ' +str(course_name) 
        }
    ), 404

@app.route("/course/id/<string:course_id>", methods=['GET'])
def get_course_by_course_id(course_id):
    course = Course.query.filter_by(course_id = course_id).first()
    if course:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": course.json()
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": str(course_id) + "id not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

def add(x,y):
    return x+y