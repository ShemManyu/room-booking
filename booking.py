import os

from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)
rooms = []
app.config['SECRET_KEY'] = '-\xeb\xa9\xcc\xad\x82\xc8*\x96;\x89<F\x83\x04|>\xf79\xcf\xee\x12\xf7\xc5'

def add_room(roomnumber, description):
    rooms.append(dict(
        roomnumber = roomnumber,
        description = description,
        date = datetime.utcnow()
    ))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        roomnumber = request.form['roomnumber']
        description = request.form['description']
        add_room(roomnumber, description)
    return render_template('index.html', rooms=rooms)

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