from . import db  # Import the db instance from the current package (assuming it's a Flask application)
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Note(db.Model):  # Define a Note model that inherits from db.Model
    id = db.Column(db.Integer, primary_key=True)  # Primary key column for Note
    data = db.Column(db.String(10000))  # Column to store note data (string up to 10000 characters)
    date = db.Column(db.DateTime(timezone=True), default=func.now())  # Column for note creation date/time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign key column referencing User table

    # Establish relationship with User model to associate notes with users
    user = relationship('User', back_populates='notes')


class User(db.Model, UserMixin):  # Define a User model that inherits from db.Model and UserMixin
    id = db.Column(db.Integer, primary_key=True)  # Primary key column for User
    email = db.Column(db.String(150), unique=True)  # Column to store user's email (unique)
    password = db.Column(db.String(150))  # Column to store user's password
    name = db.Column(db.String(150))  # Column to store user's name

    # Establish relationship with Note model to retrieve all notes associated with a user
    notes = relationship('Note', back_populates='user')

"""from . import db #from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model): #inherit from db.Module
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
   
    
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notes = db.relationship('Note')#store all notes that a user has created using relation ship
"""