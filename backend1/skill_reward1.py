from invokes import invoke_http, all_route
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


class Skill_Rewarded(db.Model):
    __tablename__ = 'Skill_Rewarded'

    Skill_Rewarded_ID = db.Column(db.Integer, primary_key=True)
    Skill_ID = db.Column(
        db.String(50), db.ForeignKey('Skill.Skill_ID'))
    Course_ID = db.Column(
        db.Integer, db.ForeignKey('Course.Course_ID'))

    def __init__(self, Skill_Rewarded_ID, Skill_ID, Course_ID):
        self.Skill_Rewarded_ID = Skill_Rewarded_ID
        self.Skill_ID = Skill_ID
        self.Course_ID = Course_ID

    def json(self):
        return {"Skill_Rewarded_ID": self.Skill_Rewarded_ID, "Skill_ID": self.Skill_ID, "Course_ID": self.Course_ID}

db.create_all()

@app.route("/view_course_skills/get_skill/<Course_ID>")
def view_skills_by_courseID(Course_ID):
    skill_rewarded_list = Skill_Rewarded.query.filter_by(Course_ID=Course_ID)
    if skill_rewarded_list:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Skill_Rewarded": [skill_rewarded.json() for skill_rewarded in skill_rewarded_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Course ID is not found. Please double check."
        }
    ), 404

@app.route("/view_course_skills/get_course/<Skill_Name>")
def view_course_by_skill_name(Skill_Name):
    #get skill data
    course_route = "http://127.0.0.1:5000/skill"
    skills = invoke_http(course_route, method='GET')
    for skill in skills['data']['skill']:
        print(skill)
        if (skill['Skill_Name'] == Skill_Name):
            Skill_ID = skill['Skill_ID']

    course_id_list = Skill_Rewarded.query.filter_by(Skill_ID=Skill_ID)
    if course_id_list:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Course List": [course.json() for course in course_id_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No course is associated with " + str(Skill_ID)
        }
    ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

