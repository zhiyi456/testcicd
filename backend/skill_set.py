from flask import jsonify, request
from __main__ import app,db
#from app import app,db

class Skill_Set(db.Model):
    __tablename__ = 'Skill_Set'

    Skill_Set_ID = db.Column(db.Integer, primary_key=True)
    Skill_Name = db.Column(
        db.String(50), db.ForeignKey('Skill.Skill_Name'))
    Position_Name = db.Column(
        db.String(50), db.ForeignKey('Positions.Position_Name'))
    

    def __init__(self, Skill_Name, Position_Name):
        if not isinstance(Skill_Name, str):
            raise TypeError("Skill_Name must be a string")
        if not isinstance(Position_Name, str):
            raise TypeError("Position_Name must be a string")
        self.Skill_Name = Skill_Name
        self.Position_Name = Position_Name

    def json(self):
        return {"Skill_Set_ID": self.Skill_Set_ID, 
                "Skill_Name": self.Skill_Name, 
                "Position_Name": self.Position_Name}

@app.route("/skill_set")  # get all skill sets
def get_all():
    skill_set = Skill_Set.query.all()
    if len(skill_set):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "skill_set": [skill.json() for skill in skill_set]
                }
            }
        )
    else:
        return jsonify({
            "message": "Skill set not found."
        }), 404

@app.route("/skill_set/<Position_Name>")  # get skills by Position_Name
def get_skills_by_position(Position_Name):
    skill_set_list = Skill_Set.query.filter_by(Position_Name=Position_Name)

    if skill_set_list:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Skill_Set": [skill_set.json() for skill_set in skill_set_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Position ID is not found. Please double check."
        }
    ), 404

@app.route("/create_new_skillset", methods=['POST']) # create skillset 
def create_new_skillset():

    data = request.get_json()
    if (Skill_Set.query.filter_by(Position_Name=data["Position_Name"], Skill_Name=data["Skill_Name"]).first()):
        return jsonify(
            {
                "code": 400,
                "data": data,
                "message": "A skillset with the same ID already exists."
            }
        ), 400

    print(data)
    skillset = Skill_Set(**data)
    print(skillset)
    try:
        db.session.add(skillset)
        db.session.commit()
    except Exception as e:
        print(e,'================================================')
        return jsonify(
            {
                "code": 500,
                "data": {
                    "New_SkillSet": data
                },
                "message": "An error occurred while creating the skillset."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": skillset.json()
        }
    ), 201


@app.route("/update_skillset", methods=['POST']) # create skillset 
def update_skillset():

    data = request.get_json()
    print(data,'============================')
    position=data['position_name']
    to_add=data['add']
    to_delete=data['delete']
    add_name=[]
    delete_name=[]
    for item in to_delete:
        delete_name.append(item)
    for item in to_add:
        add_name.append(item)
    print(delete_name,'=================================================================================================================================================================================================================================================================')
    #skillset = Skill_Set(**data)
    #print(skillset)
    # delete where position is x and skill in skill array
    # add position x and skill y
    
    try:
        for item in to_add:
            data={"Skill_Name":item,"Position_Name":position}
            skillset = Skill_Set(**data)
            db.session.add(skillset)
            db.session.commit()
        for item in to_delete :
            Skill_Set.query.filter_by(Skill_Name=item,Position_Name=position).delete()
            db.session.commit()
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "data": {
                    "New_SkillSet": 'skillset'
                },
                "message": "An error occurred while creating the skillset."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "message":"skills successfully updated!"
        }
    ), 201