from rest_framework.test import APITestCase
from datetime import datetime
from django.urls import reverse

class TestSetUp(APITestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
