from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask("test application")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.sqlite"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/", methods=["POST"])
def handler():
    print(request.form.get("age"))
    age = int(request.form.get("age"))
    if age < 18:
        return {
            "status": 'FAILURE',
            "code": 1,
            "description": "age smallar"
        }
    return {
        "status": 'OK',
        "code": 0,
        "description": "its ok"
    }


@app.route("/about")
def handler_about():
    return "OK /about"


from .oauth import oauth as oAuth
app.register_blueprint(oAuth)

from .api import api as api_
app.register_blueprint(api_)
