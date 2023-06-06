from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
import random

app = Flask("test application")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.sqlite"
db = SQLAlchemy(app)


class User(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    login = sa.Column(sa.Text, unique=True, nullable=False)
    password = sa.Column(sa.Text, nullable=False)
    date_of_birth = sa.Column(sa.DateTime)


with app.app_context():
    db.create_all()


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


@app.post("/registration")
def registration():
    login = request.form.get("login")
    passwd = request.form.get("password")
    if not login or not passwd:
        return "No such data in request"
    check_login = User.query.filter_by(login=login).first()
    if check_login:
        return "User already exist"
    user = User(login=login, password=passwd)
    db.session.add(user)
    db.session.commit()
    return "OK"


@app.post("/auth")
def auth():
    print(request)
    login = request.form.get("login")
    passwd = request.form.get("password")
    if not login or not passwd:
        return "No such data in request"
    record = User.query.filter_by(login=login).first()
    if not record or record.password != passwd:
        return "login or password not match"
    return "OK"


app.run(debug=True)
