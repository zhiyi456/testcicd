#from backend.invokes import invoke_http, all_route
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



class Skill(db.Model):
    __tablename__ = 'Skill'

    Skill_ID = db.Column(db.Integer, primary_key=True)
    Skill_Name = db.Column(db.String(50))

    def __init__(self, Skill_ID, Skill_Name):
        self.Skill_ID = Skill_ID
        self.Skill_Name = Skill_Name

    def json(self):
        return {"Skill_Name": self.Skill_Name, "Skill_ID": self.Skill_ID}

db.create_all()

@app.route("/skill")  # get all skill
def skill_get_all():
    skills = Skill.query.all()
    if skills:
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)