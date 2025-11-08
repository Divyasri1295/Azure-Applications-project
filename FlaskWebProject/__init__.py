"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
import sys

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
# Configure logging
app.logger.setLevel(logging.INFO)

# Stream logs to stdout so they appear in Azure Log Stream
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)

# Define the format
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

# Add the handler to the app's logger
if not app.logger.handlers:
    app.logger.addHandler(handler)

app.logger.info("Flask app initialized and logging configured.")

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
