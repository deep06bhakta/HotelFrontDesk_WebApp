from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    room_number = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    room_type = db.Column(db.String(100), nullable=False)
    num_days = db.Column(db.String(20), nullable=False)
    pymt_type = db.Column(db.String(100), nullable=False)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(20), unique=True, nullable=False)
    is_booked = db.Column(db.Boolean, default=False)
    is_occupied = db.Column(db.Boolean, default=False)
    needs_cleaning = db.Column(db.Boolean, default=False)
