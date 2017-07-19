from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from flask_rest_api.models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field is required")
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="This field is required")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "Item with name {} already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)

        item.save_to_db()

        return item.json(), 201

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        if item:
            item.price = data['price']
            item.price = data['store_id']
        else:
            item = ItemModel(name, **data)

        item.save_to_db()
        return item.json()

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}


class ItemList(Resource):
    def get(self):
        return {'items': [i.json() for i in ItemModel.query.all()]}
