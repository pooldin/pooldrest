import os

from flask import Flask
from pooldlib.postgresql import db


DIR = os.path.dirname(__file__)
DIR = os.path.abspath(DIR)

settings = os.environ.get('POOLDREST_CONFIG')
settings = settings or 'pooldrest.settings.dev'

# Create app
app = Flask(__name__)

# Configure the app
app.config.from_object('pooldrest.settings.base')
app.config.from_object(settings)

# Initialize database
db.init_connection(app.config)

# TODO: Register all application blueprint


# Rollback any pending transaction, close any open cursors and close any
# open connections when the application is torn down.
@app.teardown_appcontext
def shutdown_session(response):
    db.session.remove()


@app.route('/')
def index():
    return 'Hello World!'
