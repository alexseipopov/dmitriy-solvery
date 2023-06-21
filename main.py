import sqlalchemy as sa
from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask("test application")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.sqlite"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    login = sa.Column(sa.Text, unique=True, nullable=False)
    password = sa.Column(sa.Text, nullable=False)


class Card(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False)
    description = sa.Column(sa.Text)
    price = sa.Column(sa.Numeric, nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)


with app.app_context():
    db.create_all()


# CRUD - Create Read Update Delete
def create_response(status="SUCCESS", code=0, description="OK", data=None):
    if data is None:
        data = {}
    return {
            "status": status,
            "code": code,
            "description": description,
            "data": data
        }


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
        return create_response("FAILURE", 1,  "No such data in request"), 400
    check_login = User.query.filter_by(login=login).first()
    if check_login:
        return create_response("FAILURE", 2, "User already exist"), 400
    user = User(login=login, password=passwd)
    db.session.add(user)
    db.session.commit()
    return create_response(), 200


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


@app.post("/create_card")
def create_card():
    name = request.form.get("name")
    description = request.form.get("description")
    price = request.form.get("price")
    if name is None or price is None:
        return create_response("Failure", 1, "No such data in request"), 400
    card = Card(name=name, price=price, description=description)
    db.session.add(card)
    db.session.commit()
    return create_response(data={
        "id": card.id,
        "name": card.name,
        "description": card.description,
        "price": card.price,
        "is_active": card.is_active
    })


@app.get("/get_cards")
def get_cards():
    cards = Card.query.all()
    response_data = []
    for card in cards:
        response_data.append({
            "id": card.id,
            "name": card.name,
            "description": card.description,
            "price": card.price,
            "is_active": card.is_active
        })
    return create_response(data=response_data)


if __name__ == "__main__":
    app.run(debug=True, port=3010)
