from flask_restful import Resource, reqparse

from flask_rest_api.models.user import UserModel


class UserRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help="This field is required")
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help="This field is required")

        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "exists"}, 400

        UserModel(**data).save_to_db()

        return {"message": "created successfully"}, 201
