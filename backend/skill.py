from flask import jsonify
from __main__ import app,db
#from app import app,db

class Skill(db.Model):
    __tablename__ = 'Skill'
    
    Skill_Name = db.Column(db.String(50), primary_key=True)

    def __init__(self, Skill_Name):
        if not isinstance(Skill_Name, str):
            raise TypeError("Skill_Name must be a string")
        self.Skill_Name = Skill_Name

    def json(self):
        return {"Skill_Name": self.Skill_Name}

@app.route("/skill")  # get all skill
def skill_get_all():
    skills = Skill.query.all()
    if len(skills):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "skill": [skill.json() for skill in skills]
                }
            }
        )
    else:
        return jsonify({
            "message": "Skills not found."
        }), 404

@app.route("/skill/name/<string:name>", methods=['GET']) # search skill by name using wildcard
def skill_get_by_name(name):
    skill_data = Skill.query.filter(Skill.Skill_Name.like('%' + name + '%'))
    if skill_data:
        return jsonify(
            {
                "code": 200,
                "data": {
                    # "skills": skill_data
                    "skills": [skill.json() for skill in skill_data]
                }
            }
        )
    return jsonify (
        {
            "code": 404,
            "message": 'No skill named ' + str(name) 
        }
    )

@app.route("/skill/<Skill_ID>", methods=['GET'])
def get_skill_by_id(Skill_ID):
    skill_data = Skill.query.filter_by(Skill_ID=Skill_ID)
    if skill_data:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "skill": [skill.json() for skill in skill_data]
                }
            }
        )

@app.route("/skill/delete/<string:skill_name>", methods=["DELETE"]) #delete skill by name
def skill_delete_by_name(skill_name):
    # if skill doesnt exist
    if not (Skill.query.filter_by(Skill_Name=skill_name).first()):
        return jsonify(
            {
                "code": 404,
                "data": {
                    "Skill_Name": skill_name
                },
                "message": "Skill does not exist"
            }
        ), 404
    # if skill exists

    # return "returning: " + skill_name
    try:
        # Skill.query.filter_by(Skill_Name = skill_name).delete()
        result = Skill.query.filter_by(Skill_Name = skill_name).first()
        db.session.delete(result)
        db.session.commit()

    except:    
        return jsonify(
                {
                    "code": 500,
                    "data": {
                        "Skill_Name": skill_name
                    },
                    "message": "An error occurred while deleting the Skill."
                }
            ), 500

    return jsonify(
        {
            "code": 200,
            "data": skill_name
        }
    ), 200
