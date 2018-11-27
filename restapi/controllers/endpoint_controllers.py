from restapi.models.models import Users , users
from flask import json, jsonify,request , Response

def new_user():
    user = Users()
    data = request.get_json() 
    user.fname = data['fname']
    user.lname = data['lname']
    
    def id_inc():
        if len(users) == 0:
            userid = len(users)+1
        else:
            userid = users[-1]['uid']+1
        return userid

    user_dict= {
        'uid': id_inc(),
        'fname': user.fname,
        'lname': user.lname

    }


    users.append(user_dict)

    return jsonify({
            'data' : users,
            'status': 201,
            'id': user_dict['uid'],
            'message': 'Successfully added user'
        })
