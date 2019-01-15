import unittest
from restapi import app
from restapi.models.redflag_models import Redflags
from restapi.controllers.redflag_controllers import IncidentsList
import json


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        # runs at the start of @ test
        self.app = app.test_client()

    def tearDown(self):
        IncidentsList.incident_list.clear()



    def test_posts_incident(self):
    
        data = {
            "id": "1",
            "incident_type": "Redflag",
            "created_by": "gon",
            "status": "pending",
            "images": "marcus",
            "videos": "hey there",
            "comment": "corruption",
            'location': 'kampala'

        }
        res = self.app.post(
            '/api/v1/redflags', content_type='application/json', data=json.dumps(data))
        self.assertEqual(res.status_code, 201)
        response = json.loads(res.data.decode())
        self.assertEqual(response['message'], "Redflag has been created")


if __name__ == '__main__':
    unittest.main()
