# groupchat_app/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Group, GroupMessage

class GroupChatAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.admin_user = User.objects.create_superuser(username='adminuser', password='adminpassword', email='admin@example.com')

    def test_user_create(self):
        url = '/users/create/'
        data = {'username': 'newuser', 'password': 'newpassword', 'email': 'newuser@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Add more test cases for other APIs

    def test_like_unlike_message(self):
        message = GroupMessage.objects.create(group=Group.objects.create(name='Test Group'), sender=self.user, message='Test message')
        url = f'/group-messages/{message.id}/like-unlike/'
        self.client.force_authenticate(user=self.user)
        
        # Test liking the message
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user in message.likes.all())

        # Test unliking the message
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.user in message.likes.all())
