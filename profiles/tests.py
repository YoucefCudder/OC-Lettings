from django.test import TestCase, Client
from django.urls import reverse

from .models import Profile


class TestProfileViews(TestCase):
    client = Client()

    def test_profiles_index(self):
        # Call the method under test by generating the URL using the reverse function
        response = self.client.get(reverse('profiles_index'))

        # Assert that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template was used to render the response
        self.assertTemplateUsed(response, 'profiles_index.html')

        # Check that the profiles list is correct
        self.assertIn(self.client, response.context['profiles_list'])

    def test_profile(self):
        # Call the method under test by generating the URL using the reverse function
        response = self.client.get(reverse('profile', kwargs={'username': self.client.user.username}))

        # Assert that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template was used to render the response
        self.assertTemplateUsed(response, 'profile.html')

        # Check that the correct profile was passed to the template
        self.assertEqual(self.client, response.context['profile'])