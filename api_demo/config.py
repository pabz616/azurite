import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

HOST = '192.168.1.161'
BASE_URI = f'http://{HOST}:5000/api/people'
COVID_TRACKER_HOST = "http://127.0.0.1:3000"

BOOKER_URL = "https://restful-booker.herokuapp.com/booking/"
BOOKED_RESERVATION = "https://restful-booker.herokuapp.com/booking/1"
AUTH_URL = "https://restful-booker.herokuapp.com/auth"

USN = "admin"
PWD = "password123"

base_dir = os.path.abspath(os.path.dirname(__file__))

# create connexion app instance
connex_app = connexion.App(__name__, specification_dir=base_dir)

# Get underlying flask app
app = connex_app.app

# Configure SQLAlchemy part of the app instance
# Echo SQL statements it executes to console (useful to debug db programs)
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'people.db')
# Below is typically on in event driven programs
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Init marshmallow
# Used to person serialization and deserialization of SQLAlchemy models
ma = Marshmallow(app)