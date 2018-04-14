from flask import render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
#from flask_login import login_required

from booking import app, db
from booking.models import Room, Booking, User

#Fake login
def logged_in_user():
    return User.query.filter_by(username='shem').first()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        roomnumber = request.form['roomnumber']
        description = request.form['description']
        room = Room(number=roomnumber, description=description)
        db.session.add(room)
        db.session.commit()
    return render_template('index.html', rooms=Room.getall())

@app.route('/delete/<roomnumber>', methods=['GET', 'POST'])
def delete(roomnumber):
    room = Room.query.filter_by(number=roomnumber).first_or_404()
    db.session.delete(room)
    db.session.commit()
    return render_template('index.html', rooms=Room.getall())

@app.route('/room/<roomnumber>', methods=['GET', 'POST'])
def room(roomnumber):
    if request.method == "POST":
        room = Room.query.filter_by(number=roomnumber).first()
        date = request.form['date']
        start_time = request.form['from']
        end_time = request.form['to']
        roomnumber = roomnumber
        booking = Booking(date=date, start_time=start_time, end_time=end_time, room= room)
        db.session.add(booking)
        db.session.commit()
    return render_template('room.html', room=Room.query.filter_by(number=roomnumber).first(), bookings=Booking.getroombooking(roomnumber))

@app.route('/remove/<roomnumber>/<bookingid>', methods=['GET', 'POST'])
def remove(roomnumber, bookingid):
    booking = Booking.query.filter_by(id=bookingid).first_or_404()
    db.session.delete(booking)
    db.session.commit()
    return render_template('room.html', room=Room.query.filter_by(number=roomnumber).first(), bookings=Booking.getroombooking(roomnumber))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)