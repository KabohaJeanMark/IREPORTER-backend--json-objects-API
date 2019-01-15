from flask import request, jsonify
from restapi.models.user_models import Users, BaseUsers, UsersDB

UsersList = UsersDB()


class UserController:

    def __init__(self):
        pass

    def create_users(self):
        data = request.get_json()

        first_name = data["first_name"]
        last_name = data["last_name"]
        other_names = data["other_names"]
        phone_number = data.get("phone_number")
        user_id = len(UsersList.user_list) + 1
        user_name = data.get("user_name")
        email = data.get("email")
        is_admin = data.get("is_admin")

        myUser = Users(BaseUsers(
            first_name, last_name, other_names, phone_number), user_id, user_name, email, is_admin)

        UsersList.add_user(myUser)
        return jsonify({
            "status": 201,
            "data": [{
                "id": myUser.user_id,
                "message": "Created new user"
            }]
        })

    def get_all_users(self):
        return jsonify({
            "status": 200,
            "data": [user.to_json() for user in UsersList.user_list]
        })

    def get_a_single_user(self, user_id):
        user = UsersList.get_one_user_by_id(user_id)
        if user:
            return jsonify({
                "status": 200,
                "data": user.to_json()
            })
        else:
            return jsonify({
                "status": 404,
                "message": "That user id is not found"
            })
