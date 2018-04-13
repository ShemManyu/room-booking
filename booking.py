from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)
rooms = []
app.config['SECRET_KEY'] = '-\xeb\xa9\xcc\xad\x82\xc8*\x96;\x89<F\x83\x04|>\xf79\xcf\xee\x12\xf7\xc5'

def add_room(roomnumber):
    rooms.append(dict(
        roomnumber = roomnumber,
        user = "shem",
        date = datetime.utcnow()
    ))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        roomnumber = request.form['roomnumber']
        add_room(roomnumber)
    return render_template('index.html', rooms=rooms)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)