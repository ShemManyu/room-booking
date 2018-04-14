from flask import render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

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

@app.route('/room', methods=['GET', 'POST'])
def room():
    return render_template('room.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)