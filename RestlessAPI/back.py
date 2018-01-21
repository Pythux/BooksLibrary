#!/usr/bin/env python3
import os
import re

import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from flask_restless import APIManager


class ValidationError(Exception):
    pass


app = flask.Flask(__name__)

app.config['DEBUG'] = True
path_sqlite = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'sqlite.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path_sqlite # 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


many_many_author_book = db.Table('many_many_author_book',
    db.Column('author_id', db.Integer,
              db.ForeignKey('author.id'), primary_key=True),
    db.Column('book_id', db.Integer,
              db.ForeignKey('book.id'), primary_key=True),
)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Unicode(80), nullable=False)
    last_name = db.Column(db.Unicode(80), nullable=False)
    books = db.relationship('Book',
                            secondary=many_many_author_book,
                            lazy=True,
                            backref=db.backref('authors'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


ISBN_VALIDATOR = re.compile(
    # regex=r'^(ISBN[-]*(1[03])*[ ]*(: ){0,1})*' ...
    r'(([0-9Xx][- ]*){13}|([0-9Xx][- ]*){10})$')


many_many_book_subject = db.Table('many_many_book_subject',
    db.Column('book_id', db.Integer,
              db.ForeignKey('book.id'), primary_key=True),
    db.Column('subject_id', db.Integer,
              db.ForeignKey('subject.id'), primary_key=True),
)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(28), unique=True)
    title = db.Column(db.Unicode(200), nullable=False)
    description = db.Column(db.Unicode(), nullable=True)
    subjects = db.relationship('Subject',
                               secondary=many_many_book_subject,
                               backref=db.backref('books', lazy=True))

    @validates('isbn')
    def validate_isbn(self, key, isbn):
        if not ISBN_VALIDATOR.match(isbn):
            exception = ValidationError()
            exception.errors = {
                'isbn': 'must match pattern: {}'.format(
                    ISBN_VALIDATOR.pattern)}
            raise exception
        return isbn


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.Unicode(80), unique=True)

    def __str__(self):
        return str(self.name).capitalize()


@app.after_request
def add_cors_headers(response):
    # allow GET from crossorigin (like another port on localhost)
    response.headers['Access-Control-Allow-Origin'] = '*'  # http://localhost:8080

    response.headers['Access-Control-Allow-Methods'] = \
        'GET, OPTIONS, POST, DELETE, PUT, PATCH'
    """The Access-Control-Allow-Methods response header
    specifies the method or methods allowed
    when accessing the resource in response to a preflight request.

    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods"""

    # allow POST on crossorigin (it will make a OPTIONS to know it)
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


if __name__ == '__main__':
    db.create_all()

    manager = APIManager(app, flask_sqlalchemy_db=db)
    # which will be available at /api/<tablename> by default.
    allowed_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    blueprint = manager.create_api(Book, methods=allowed_methods,
                                   collection_name='books',
                                   validation_exceptions=[ValidationError])
    manager.create_api(Author, methods=allowed_methods, collection_name='authors')
    manager.create_api(Subject, methods=allowed_methods,
                       collection_name='subjects',
                       primary_key='subject',
                       exclude_columns=[])
    # start the flask loop
    app.run()

"""
pip install Flask-Restless
pip install httpie

http OPTIONS :5000/api/books
http OPTIONS :5000/api/books/<book_id>

http POST :5000/api/subjects subject=fantasy
http POST :5000/api/subjects subject=thriller

http POST :5000/api/authors first_name=John last_name=Doe

http POST :5000/api/books title='a book' isbn=978-2-8688-9006-1
http PUT :5000/api/books/1 title='a book' isbn=978-2-8688-9006-1 subjects:='[{"id": 1}]' authors:='[{"id": 1}]'

http GET :5000/api/books

http PATCH :5000/api/books/1 title='better stronger faster'


"""
