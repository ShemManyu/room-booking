import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '-\xeb\xa9\xcc\xad\x82\xc8*\x96;\x89<F\x83\x04|>\xf79\xcf\xee\x12\xf7\xc5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#configure auth
#login_manager = LoginManager()
#login_manager.session_protection = "strong"
#login_manager.init_app(app)

from booking import models, views