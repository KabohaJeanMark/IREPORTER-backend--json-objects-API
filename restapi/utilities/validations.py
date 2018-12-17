import string
from restapi.models.models import incidents
#naming convention for predicates. statr with is
def checks_empty_fields(*fields):
    """the function that checks for an empty field"""
    for field in fields:
        if not field:
            return "invalid"
    return "valid"
#holistic thinking
def check_field_types(location,images,video,comment):
    """ function that checks if the types are string"""
    if isinstance(images, str) and isinstance(video, str) \
             and isinstance(comment,str) and isinstance(location, str): 
        return True 

def avoid_white_space_char(*fields):
    """function that removes white spaces from the field"""
    for field in fields:
        if not field.strip():
            return True

def validate_status(status):
    """function that validates status"""
    if status != "pending" and status != "investigation" and status != "resolved" and status != "rejected":
        return True #false, explicit, naming, logic,



