from flask import Flask,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app= Flask(__name__,template_folder="template")


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({ 
        'name' : 'rahulsiva',
        'message': 'hello world'
        })


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.column(db.string(20))
    contact = db.column(db.String(100), unique=True)

    def __init__(self, name, contact):
        self.name=name
        self.contact=contact

class UserSchema(ma.Schema):
    class meta:
        fields = ('id', 'name', 'contact')


user_schema = UserSchema()
users_schema = UserSchema(many=True)




if __name__ == "__main__":
    app.run(debug=True)