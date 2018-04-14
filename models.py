from datetime import datetime

from sqlalchemy import desc
from flask_login import UserMixin

from booking import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return "<User {}> ".format(self.username)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Text, nullable=False)
    start_time = db.Column(db.Text, nullable=False)
    end_time = db.Column(db.Text, nullable=False)

    room_number = db.Column(db.Integer, db.ForeignKey('room.number'), nullable=False)
    room = db.relationship('Room', backref=db.backref('posts', lazy=True))

    @staticmethod
    def getroombooking(num):
        return Booking.query.filter_by(room_number=num).all()

    def __repr__(self):
        return "<Booking date '{}' start '{}' end '{}' >".format(self.date, self.start_time, self.end_time)

class Room(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)

    @staticmethod
    def getall():
        return Room.query.all()

    def __repr__(self):
        return "<Room '{}': '{}'>".format(self.number, self.description)