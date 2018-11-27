from restapi.models.models import Users , users , Incidents , incidents
from flask import json, jsonify,request , Response
import datetime 

def id_generate(my_list):
        if len(my_list) == 0:
            iid = len(my_list)+1
        else:
            iid = my_list[-1]['iid']+1
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
        'iid': id_generate(users),
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
            'id': user_dict['iid'],
            'message': 'Successfully added user'
        })

def new_incident():
    incident= Incidents()
    data = request.get_json()
    incident.created_by=data['createdBy']
    #r = requests.get('http://127.0.0.1:5000/api/v1/redflag')
    incident.created_on = datetime.datetime.now()
    #incident.created_by = r.headers.createdBy 
    incident.incident_type = data['incidentType']
    incident.location = data['location']
    incident.status = data['status']
    incident.images = data['images']
    incident.videos = data['videos']
    incident.comment = data['comment']

    incident_dic={
        'iid': id_generate(incidents),
        'createdOn': incident.created_on,
        'createdBy': incident.created_by,
        'incidentType': incident.incident_type,
        'location': incident.location,
        'status': incident.status,
        'images': incident.images,
        'videos': incident.videos,
        'comment': incident.comment
    }

    incidents.append(incident_dic)
    return jsonify({
            'data' : incidents,
            'status': 201,
            'id': incident_dic['iid'],
            'message': 'Successfully added incident'
        })

"""
def add_redflag():
    redFlag = RedFlags()
    data = request.get_json()
    redFlag.created_on = data['created_on']
    redFlag.created_by = data['created_by']
    redFlag.incident_type = data['incident_type']
    redFlag.location = data['location']
    redFlag.status = data['status']
    redFlag.images = data['images']
    redFlag.videos = data['videos']
    redFlag.comment = data['comment']
    redFlag.red_flag = data['red_flag']

    redflag_dict = {
        'iid': id_generate(incidents),
        'createdOn': redFlag.created_on,
        'createdBy': redFlag.created_by,
        'incidentType': redFlag.incident_type,
        'location': redFlag.location,
        'status': redFlag.status,
        'images': redFlag.images,
        'videos': redFlag.videos,
        'comment': redFlag.comment,
        'red_flag': redFlag.red_flag
    }
    incidents.append(redflag_dict)
    return incidents
"""
"""
def add_intervention():
    intervention = Interventions()
    data = request.get_json()
    intervention.created_on = data['created_on']
    intervention.created_by = data['created_by']
    intervention.incident_type = data['incident_type']
    intervention.location = data['location']
    intervention.status = data['status']
    intervention.images = data['images']
    intervention.videos = data['videos']
    intervention.comment = data['comment']
    intervention.interventions = data['interventions']

    interventions_dict = {
        'iid': id_generate(incidents),
        'created_on': intervention.created_on,
        'created_by': intervention.created_by,
        'incident_type': intervention.incident_type,
        'location': intervention.location,
        'status': intervention.status,
        'images': intervention.images,
        'videos': intervention.videos,
        'comment': intervention.comment,
        'red_flag': intervention.interventions
    }
    incidents.append(interventions_dict)
    return incidents
"""