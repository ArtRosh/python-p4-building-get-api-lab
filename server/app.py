#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from sqlalchemy import desc

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():

    bakeries = [b.to_dict() for b in Bakery.query.all()]

    response = make_response(
        jsonify(bakeries), 
        200
    )

    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):

    bakeries_by_id = Bakery.query.filter(Bakery.id == id).first()

    bakaries_to_dict = bakeries_by_id.to_dict()

    response = make_response(
        jsonify(bakaries_to_dict),
        200
    )

    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():

    bakeries_by_price = BakedGood.query.order_by(desc(BakedGood.price)).all()

    bakeries_to_dict = [b.to_dict() for b in bakeries_by_price]

    response = make_response(
        jsonify(bakeries_to_dict),
        200
    )
    
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():

    most_expensive_baked_good = BakedGood.query.order_by(desc(BakedGood.price)).first()

    baked_good_to_dict = most_expensive_baked_good.to_dict()

    response = make_response(
        jsonify(baked_good_to_dict),
        200
    )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
