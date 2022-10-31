from flask import request, jsonify
from __main__ import app,db


class LearningJourney(db.Model):
    __tablename__ = 'Learning_Journey'
        
    Learning_Journey_ID = db.Column(db.Integer, primary_key=True)
    Staff_ID = db.Column(db.Integer, db.ForeignKey('Staff.Staff_ID'))
    Position_Name = db.Column(db.String(50), db.ForeignKey('Positions.Position_Name'))
    Skill_Name = db.Column(db.String(50), db.ForeignKey('Skill.Skill_Name'))
    Course_ID = db.Column(db.String(50), db.ForeignKey('Course.Course_ID'))

    def __init__(self, Staff_ID, Position_Name, Skill_Name, Course_ID):
        if not isinstance(Staff_ID, int):
            raise TypeError("Staff_ID must be an integer")
        if not isinstance(Position_Name, str):
            raise TypeError("Position_Name must be an integer")
        if not isinstance(Skill_Name, str):
            raise TypeError("Skill_Name must be a string")
        if not isinstance(Course_ID, str):
            raise TypeError("Course_ID must be an string")
        self.Staff_ID = Staff_ID
        self.Position_Name = Position_Name
        self.Skill_Name = Skill_Name
        self.Course_ID = Course_ID

    def json(self):
        return {
            "Learning_Journey_ID": self.Learning_Journey_ID,
            "Staff_ID": self.Staff_ID,
            "Position_Name": self.Position_Name,
            "Skill_Name": self.Skill_Name,
            "Course_ID": self.Course_ID
        }

@app.route("/get_learning_journey")
def get_learning_journey():
    lj_list = LearningJourney.query.all()
    if len(lj_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lj": [lj.json() for lj in lj_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Learning Journey."
        }
    ), 404


@app.route("/get_learning_journey_by_staff_id/<Staff_ID>")
def get_learning_journey_by_staff_id(Staff_ID):
    lj_list = LearningJourney.query.filter_by(Staff_ID=Staff_ID).all()
    if len(lj_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lj": [lj.json() for lj in lj_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": Staff_ID +" has no Learning Journey."
        }
    ), 404


@app.route("/get_learning_journey_by_lj_id/<Learning_Journey_ID>")
def get_learning_journey_by_lj_id(Learning_Journey_ID):
    lj_list = LearningJourney.query.filter_by(Learning_Journey_ID=Learning_Journey_ID).all()

    if len(lj_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lj": [lj.json() for lj in lj_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Learning Journey ID do not exist."
        }
    ), 404

@app.route("/create_learning_journey", methods=['POST'])
def create_learning_journey():

    data = request.get_json()
    lj = LearningJourney(**data)
    db.session.add(lj)
    db.session.commit()
    try:
        print("Hello")  
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Learning_Journey": data
                },
                "message": "An error occurred creating the Learning Journey."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": data
        }
    ), 201


    