from flask import request, jsonify
from datetime import datetime
from restapi.models.redflag_models import Redflags, BaseRedFlags, RedFlagsDb


IncidentsList = RedFlagsDb()


class RedFlagsController():

    def __init__(self):
        pass

    def create_redflag(self):
        data = request.get_json()

        created_by = data.get("created_by")
        incident_type = data.get("incident_type")
        redflag_id = len(IncidentsList.incident_list) + 1
        status = data.get("status")
        images = data.get("images")
        videos = data.get("videos")
        comment = data.get("comment")
        location = data.get("location")

        myredflag = Redflags(BaseRedFlags(
            created_by, incident_type), redflag_id, status, images, videos, comment, location)

        IncidentsList.add_redflag(myredflag)
        return jsonify({
            "status": 201,
            "data": [{
                "id": myredflag.redflag_id,
                "message": "Created red-flag record"

            }]

        })

    def get_all_redflags(self):
        return jsonify({
            "status": 200,
            "data": [redflag.to_json() for redflag in IncidentsList.incident_list]

        })

    def get_a_single_redflag(self, redflag_id):

        red = IncidentsList.get_one_redflag_by_id(redflag_id)

        return jsonify({
            "status": 200,
            "data": red.to_json()
        })

    def delete_redflag(self, redflag_id):
        red = IncidentsList.get_one_redflag_by_id(redflag_id)
        if red:
            IncidentsList.incident_list.remove(red)
            return jsonify({
                "status": 200,
                "message": "Successfully deleted"
            })
        return jsonify({
            "status": 200,
            "message": "That redflag id is not found"
        })
    def update_redflag_status(self, redflag_id):
        red = IncidentsList.get_one_redflag_by_id(redflag_id)
        if red:
            red.status = request.get_json('status')
            return jsonify({
                "status": 200,
                "message": "Updated red-flag record's location",
                "new status": red.location.get('status')
            })

        return jsonify({
            "status": 200,
            "message": "That red-flag id is not found",


        })
    def update_redflag_location(self, redflag_id):
        red = IncidentsList.get_one_redflag_by_id(redflag_id)
        if red:
            red.location = request.get_json('location')
            return jsonify({
                "status": 200,
                "message": "Updated red-flag record's location",
                "new location": red.location.get('location')
            })

        return jsonify({
            "status": 200,
            "message": "That red-flag id is not found",


        })

    def update_redflag_comment(self, redflag_id):
        red = IncidentsList.get_one_redflag_by_id(redflag_id)
        if red:
            red.comment = request.get_json('comment')
            return jsonify({
                "status": 200,
                "message": "Updated red-flag record's comment",
                "new comment": red.location.get('comment')
            })

        return jsonify({
            "status": 200,
            "message": "That red-flag id is not found",


        })