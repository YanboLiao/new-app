from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True  # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = [
    {
        "name": "example_item",
        "price": 9.98
    }
]


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        # data = request.get_json()
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><br><p>V2 is deployed</p>"


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)  # important to mention debug=True
