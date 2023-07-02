from flask import request

from .. import oauth
from ... import db
from ...models.model import User
from ...utils import create_response


@oauth.post("/registration")
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


@oauth.post("/auth")
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
