import unittest
from restapi import app
from restapi.models.redflag_models import Redflags
from restapi.controllers.redflag_controllers import IncidentsList
import json


class TestEndpoints(unittest.TestCase):
    def setUp(self):

        self.app = app.test_client()

    def tearDown(self):
        IncidentsList.incident_list.clear()

    def test_index(self):
        response = self.app.get('/api/v1/')
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {
            "Message":"Welcome to Ireporter"}
        self.assertEqual(json.loads(data), message)


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
        self.assertEqual(response['status'], 201)
        

if __name__ == '__main__':
    unittest.main()
