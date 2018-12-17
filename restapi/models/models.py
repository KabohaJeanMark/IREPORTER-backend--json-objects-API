class Users:

    def __init__(self, first_name="",last_name="",other_names="",email="",phone_number="",user_name="",registered="",is_admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.other_names = other_names
        self.email = email
        self.phone_number = phone_number
        self.user_name = user_name
        self.registered = registered
        self.is_admin = is_admin

users = []

class Incidents:
    def __init__(self, created_on="",created_by="",incident_type="",location="",status="",images="",videos="",comment=""):
        self.created_on = created_on
        self.created_by = created_by
        self.incident_type = incident_type
        self.location = location
        self.status = status
        self.images = images
        self.videos = videos
        self.comment = comment

incidents = []

class RedFlags(Incidents):
   pass


class Interventions(Incidents):
   pass

