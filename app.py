from flask import Flask
from flask_migrate import Migrate
from models import db

#Heart of the application
app = Flask(__name__)


# Configuration for database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecom.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize flask migrate
migrate = Migrate(app, db)


# intialize the app to use sqlalchemy
db.init_app(app)

#flask cli
#inform the cli about the flask app and the port to use