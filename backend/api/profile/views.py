from flask import request

from .utils import prepare_data
from .. import api
from ... import db
from ...models.model import Card
from ...utils import create_response


@api.post("/card")
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


@api.get("/card")
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


@api.patch("/card")
def change_card():
    id = request.form.get("id")
    if not id:
        return create_response("Failure", 1, "No such data in request"), 400
    card = Card.query.filter_by(id=id).first()
    if not card:
        return create_response("FAILURE", 3, "no such info in db")
    data = prepare_data(request)

    card.name = data["name"] if "name" in data else card.name
    card.description = data["description"] if "description" in data else card.description
    card.price = data["price"] if "price" in data else card.price

    db.session.commit()

    print(data)
    return create_response()


@api.delete("/card")
def delete_card():
    id = request.form.get("id")
    if not id:
        return create_response("Failure", 1, "No such data in request"), 400
    card = Card.query.filter_by(id=id).first()
    db.session.delete(card)
    db.session.commit()
    return create_response()
