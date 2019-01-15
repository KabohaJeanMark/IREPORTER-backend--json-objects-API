"""File to handle tests for all endpoints """
import unittest
from restapi import app
from restapi.models.redflag_models import Redflags
from restapi.controllers.redflag_controllers import IncidentsList
import json


class TestEndPoints(unittest.TestCase):
    """ Class for testing the endpoints and their validations """
    def setUp(self):
        self.app = app.test_client()

    def tear_down(self):
        IncidentsList.incident_list.clear()

    def test_index(self):
        response = self.app.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        message = {
            "Message": "Welcome to Ireporter"}
        self.assertEqual(json.loads(data), message)

    def test_redflag_posts_incident(self):
        """A test for the post red flag endpoint """
        data = {

            "incident_type": "Redflag",
            "status": "pending",
            "images": ["image1", "image2"],
            "videos": ["video1", "video2"],
            "comment": "corruption",
            "location": {"latitude": "98899", "longitude": "888484"}



        }

        res = self.app.post(
            '/api/v1/redflags', content_type='application/json', data=json.dumps(data))
        self.assertEqual(res.status_code, 201)
        response = json.loads(res.data.decode())
        d = response['data']
        self.assertEqual(response['status'], 201)
        self.assertEqual(d[0]['message'], "Created red-flag record")

    def test_redflag_post_invalid_images_or_videos(self):
        """ A test to check out the list validation"""
        data = {
            "incident_type": "Redflag",
            "status": "pending",
            "images": "image1",
            "videos": "video1",
            "comment": "corruption",
            "location": {"latitude": "98899", "longitude": "888484"}

        }
        res = self.app.post(
            '/api/v1/redflags', content_type='application/json', data=json.dumps(data))
        response = json.loads(res.data.decode())
        self.assertEqual(response['status'], "404")
        self.assertEqual(response['message'],
                         "Images or videos should be in lists")

    def test_redflag_post_invalid_location(self):
        """A test to check out the location validation"""
        data = {
            "incident_type": "Redflag",
            "status": "pending",
            "images": "image1",
            "videos": "video1",
            "comment": "corruption",
            "location": "0887 , 8098"
        }

        res = self.app.post(
            '/api/v1/redflags', content_type='application/json', data=json.dumps(data))
        response = json.loads(res.data.decode())
        self.assertEqual(response['status'], "404")
        self.assertEqual(
            response['message'], "location should be a dictionary of latitude and logitude coordinates")

    def test_redflag_post_invalid_incident_type(self):
        """A test to confirm the incident type"""
        data = {
            "incident_type": "Ruby",
            "status": "pending",
            "images": "image1",
            "videos": "video1",
            "comment": "corruption",
            "location": "0887 , 8098"
        }

        res = self.app.post(
            '/api/v1/redflags', content_type='application/json', data=json.dumps(data))
        response = json.loads(res.data.decode())
        self.assertEqual(response['status'], "404")
        self.assertEqual(
            response['message'], "the incident should be either a redflag or intervention")

    def test_redflag_post_missing_fields(self):
        """A test to confirm missing fields"""
        data = {
            "incident_type": "Redflag",
            "status": "pending",
            "images": ["image1", "image2"],
            "comment": "corruption",
            "location": {"latitude": "98899", "longitude": "888484"}
        }

        res = self.app.post(
            '/api/v1/redflags', content_type='application/json', data=json.dumps(data))
        response = json.loads(res.data.decode())
        self.assertEqual(response['status'], "404")
        self.assertEqual(
            response['message'], "Required fields are missing. Either created_by, incident_type, images, videos, comment or location")

    def test_get_all_redflags(self):
        """ Test route for getting all incidents """
        response = self.app.get('/api/v1/redflags')
        self.assertEqual(response.status_code, 200)

    def test_get_a_single_redflag(self):
        """ Test route for getting a single red flag """
        response = self.app.get(
            '/api/v1/auth/redflags/1')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
