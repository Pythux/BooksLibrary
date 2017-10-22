import flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager


app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)

    def __repr__(self):
        return '<User %r>' % self.name


# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)
# Create API endpoints,
# which will be available at /api/<tablename> by default.
manager.create_api(Person, methods=['GET', 'POST', 'PUT', 'DELETE'])

# start the flask loop
app.run()

"""
pip install httpie

http OPTIONS :5000/api/person
http OPTIONS :5000/api/person/4

http POST :5000/api/person name=John
http POST :5000/api/person name=Kamel
http GET :5000/api/person
http PUT :5000/api/person/2 name=Joan
http DELETE :5000/api/person/1
"""
