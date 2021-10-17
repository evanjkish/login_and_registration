from flask import Flask

from flask_app.models.model_user import DATABASE
app = Flask(__name__)
app.secret_key = "shhhhhh"

DATABASE = 'login_and_registration_db'

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)