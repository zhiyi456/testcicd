
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

class Role(db.Model):
    tablename = 'Role'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False)

    def __init__(self, role_id, role_name):
        self.role_id = role_id
        self.role_name = role_name

    def json(self):
        dto = {
            'role_id': self.role_id,
            'role_name': self.role_name,
        }

        return dto

db.create_all()
# Method
@app.route("/role")
def role_get_all():
    role_list = Role.query.all()
    if len(role_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "roles": [role.json() for role in role_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Roles."
        }
    ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)