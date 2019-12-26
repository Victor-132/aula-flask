from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

database = SQLAlchemy(app)
migrate = Migrate(app, database)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager(app)

from app.models import tables, forms
from app.controllers import default