from flask import Flask
from .controllers.views import app
from .models import models

#connect sqlalchemyto app
models.db.init_app(app)

@app.cli.command("init_db")
def init_db():
    models.init_db()