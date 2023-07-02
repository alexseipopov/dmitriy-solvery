from backend import db, app
import sqlalchemy as sa


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


# http://127.0.01:5000/api/card
with app.app_context():
    db.create_all()
