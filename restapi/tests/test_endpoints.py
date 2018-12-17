import unittest
from restapi import app
from restapi.models.models import incidents
import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
         # runs at the start of @ test
         self.app = app.test_client()

    def tearDown(self):
        incidents.clear()

    
    def test_posts_incident(self):
        data = {		
		
        "location": "05858,955795",
        "videos": "video,video",
        "images":"image,image",
        "comment": 1
       
}
        res = self.app.post('/api/v1/redflags', content_type = 'application/json', data = json.dumps(data))
        self.assertEqual(res.status_code, 500)
        print(res.data)
        self.assertIn('They should all be strings', str(res.data))