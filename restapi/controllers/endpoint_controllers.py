from restapi.models.models import Users , users , Incidents , incidents
from flask import json, jsonify,request , Response
from restapi.utilities.validations import checks_empty_fields, check_field_types, avoid_white_space_char, validate_status
import datetime 

def id_generate(my_list):
        if len(my_list) == 0:
            iid = len(my_list)+1
        else:
            iid = my_list[-1]['id']+1
        return iid


def new_user():
  

    user = Users()
    data = request.get_json() 
    user.first_name = data['firstName']
    user.last_name = data['lastName']
    user.other_names = data['otherNames']
    user.email = data['email']
    user.phone_number = data['phoneNumber']
    user.user_name = data['userName']
    user.registered = datetime.datetime.now()

    
    
    user_dict= {
        'id': id_generate(users),
        'firstName': user.first_name,
        'lastName': user.last_name,
        'otherNames': user.other_names,
        'email': user.email,
        'phoneNumber': user.phone_number,
        'userName': user.user_name,
        'registered': user.registered
    }


    users.append(user_dict)

    return jsonify({
            'data' : users,
            'status': 201,
            'id': user_dict['id'],
            'message': 'Successfully added user'
        })

def new_incident():

    data = request.get_json()
    created_on = datetime.datetime.now()
    created_by = request.headers['createdBy']
    location = data['location']
    status = "pending"
    images = data['images']
    videos = data['videos']
    comment = data['comment']

    if not images or not location or not comment or not videos:
         return jsonify({'error': 'required field missing'}), 400

    # checks for the empty fields in the field in the post endpoint
    if checks_empty_fields(data['location'],
                           data['images'], data['videos'],data['comment'] ):
        return jsonify({'error': 'some fields are missing'}), 400

    # validates respective data types
    if not check_field_types(data['location'],
                           data['images'], data['videos'],data['comment']):
        return jsonify({'error': 'They should all be strings'}), 200

    # checks for whites spaces in the field
    if avoid_white_space_char(data['location'],
                           data['images'], data['videos'],data['comment'] ):
        return jsonify({'error': 'The fields contains white spaces'}), 200



    incident= Incidents()

    incident_dic={
        'id': id_generate(incidents),
        'createdOn': created_on,
        'createdBy': created_by,
        'location': location.split(","),
        'status': status,
        'images': images.split(","),
        'videos': videos.split(","),
        'comment':comment
        }
    incidents.append(incident_dic)

    return jsonify({
            'data' : incidents,
            'status': 201,
            'id': id_generate(incidents),
            'message': 'Successfully added incident'
        })

def get_all_incidents():

    return jsonify({
            'data' : incidents,
            'status': 200,
            'message': 'Successfully returned all incidents'
        })

def get_one_incident(redflagid):
    data = request.get_json()
    if 0 < redflagid <= len(incidents):
        incident = [incident for incident in incidents if incident['id'] == redflagid]
        return jsonify({
        'data': incident[0],
        'status': 200,
        'id': id_generate(incidents),
        'message':'You have got your particular redflag'
        })
    else:
        return jsonify({'message': 'redflag not found'}), 200

def new_comment(redflagid):
    data = request.get_json()
    if 0 < redflagid <= len(incidents):
        incident = [incident for incident in incidents if incident['id'] == redflagid]
        incident[0]['comment'] = data['comment']

        return jsonify({
        'data': incident,
        'status': 201,
        'id': id_generate(incidents),
        'message':"Red-flag's record comment has been updated"
        })
    else:
        return jsonify({'message': 'redflag not found'}), 200
#break controllers down
def new_location(redflagid):
    data = request.get_json()
    if 0 < redflagid <= len(incidents):
        incident = [incident for incident in incidents if incident['id'] == redflagid]
        incident[0]['location'] = data['location']
        return jsonify({
        'data': incident,
        'status': 201,
        'id': id_generate(incidents),
        'message':"Red-flag's record location has been updated"
        })
    else:
        return jsonify({'message': 'redflag not found'}), 200


def delete_flag(redflagid):
    data = request.get_json()
    if 0 < redflagid <= len(incidents):
        incident = [incident for incident in incidents if incident['id'] == redflagid]
        incidents.remove(incident[0])
        return jsonify({
        'data': incidents,
        'status': 200,
        'id': id_generate(incidents),
        'message':'Red-flag record has been deleted'
        })
    else:
        return jsonify({'message': 'red-flag not found.'}), 200

def update_status(redflagid):
    data = request.get_json()
    if validate_status(data['status']):
        return jsonify({'error': 'wrong status'}), 200
    if 0 < redflagid <= len(incidents):
        incident = [incident for incident in incidents if incident['id'] == redflagid]
        incident[0]['status']= data['status']
        return jsonify({
        'data': incident,
        'status': 200,
        'id': id_generate(incidents),
        'message':'your status has been successfully updated'
        })
    else:
        return jsonify({'message': 'redflag not found'}), 200