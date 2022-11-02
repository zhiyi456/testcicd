from flask import request, jsonify
from __main__ import app,db
from invokes import invoke_http


class Positions(db.Model):
    __tablename__ = 'Positions'

    Position_Name = db.Column(db.String(50), primary_key=True)
    #skillset = db.relationship("Skill_Set", passive_deletes=True,cascade='all,delete')
    #lj = db.relationship("LearningJourney", passive_deletes=True,cascade='all,delete')


 
    def __init__(self, Position_Name):
        if not isinstance(Position_Name, str):
            raise TypeError("Position_Name must be a string")
        self.Position_Name = Position_Name

    def json(self):
        return {"Position_Name": self.Position_Name}

@app.route("/positions")
def position_get_all():
    position_list = Positions.query.all()
    if position_list:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "positions": [position.json() for position in position_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Positions."
        }
    ), 404

@app.route("/get_position_by_name/<Position_Name>")
def get_position_by_name(Position_Name):
    position_list = Positions.query.filter_by(Position_Name=Position_Name)
    if position_list:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Positions": [position.json() for position in position_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Position is not found. Please double check."
        }
    ), 404

@app.route("/get_position/<Position_Name>")
def get_position(Position_Name):
    position_list = Positions.query.filter_by(Position_Name=Position_Name)
    if position_list:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Positions": [position.json() for position in position_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Position is not found. Please double check."
        }
    ), 404

@app.route("/create_new_position/<string:new_position>", methods=['POST'])
def create_new_position(new_position):
    if (Positions.query.filter_by(Position_Name=new_position).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "Position_Name": new_position
                },
                "message": "Position already exists."
            }
        ), 400

    data = request.get_json()
    position = Positions(**data)

    try:
        db.session.add(position)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Position_Name": position
                },
                "message": "An error occurred creating the Position."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": position.json()
        }
    ), 201


@app.route("/position/update", methods=['POST'])
def update_position_name():

    #lj_result=invoke_http("http://127.0.0.1:5000/lj", method='POST', json=None)
    
    #print(skillset_result,'========================================================================================================================================================================================================================================================================================================================================================================================================================================================')
    #print(lj_result,'========================================================================================================================================================================================================================================================================================================================================================================================================================================================')
    data = request.get_json()
    old_position_name=data['old_position_name']
    new_position_name=data['new_position_name']
   


    print(new_position_name,old_position_name,'==========================================================================================================================================================================================================================================================================================================================================================================================')
    
    result=Positions.query.filter(Positions.Position_Name==old_position_name).update({'Position_Name': new_position_name})
    #skillset_result = invoke_http("http://127.0.0.1:5000/skill_set/update_position", method='POST', json=data)
    #lj_result=invoke_http("http://127.0.0.1:5000/lj", method='POST', json=None)

    db.session.commit()
    if 'a':
        return jsonify(
            {
                "code": 200,
                "data": {
                    "skill": 'slayed'
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Skill ID is not found. Please double check."
        }
    ), 404