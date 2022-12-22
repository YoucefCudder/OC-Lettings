# from django.test import TestCase, Client
# from django.urls import reverse
#
# from .models import Profile
#
#
# class TestProfileViews(TestCase):
#     client = Client()
#
#     def test_profiles_index(self):
#         # Call the method under test by generating the URL using the reverse function
#         response = self.client.get(reverse('profiles_index'))
#
#         # Assert that the response has a 200 status code
#         self.assertEqual(response.status_code, 200)
#
#         # Assert that the correct template was used to render the response
#         self.assertTemplateUsed(response, 'profiles_index.html')
#
#         # Check that the profiles list is correct
#         self.assertIn(self.client, response.context['profiles_list'])
#
#     def test_profile(self):
#         # Call the method under test by generating the URL using the reverse function
#         response = self.client.get(reverse('profile', kwargs={'username': self.client.user.username}))
#
#         # Assert that the response has a 200 status code
#         self.assertEqual(response.status_code, 200)
#
#         # Assert that the correct template was used to render the response
#         self.assertTemplateUsed(response, 'profile.html')
#
#         # Check that the correct profile was passed to the template
#         self.assertEqual(self.client, response.context['profile'])
import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from .models import Profile
from .views import profiles_index, profile
from pytest_django.asserts import assertTemplateUsed
client = Client()

@pytest.mark.django_db
def test_profiles_index(request):
    # Profile.objects.create(user__username='test_user_2')

    # response = profiles_index(request)
    response = client.get(reverse('profiles_index'))

    # Assert that the method returns a response with the correct template
    # assert response.name == 'profiles_index.html'
    assert response.status_code == 200
    # Assert that the correct data was passed to the template
    assert 'profiles_list' in response.context
    assertTemplateUsed(response, "profiles_index.html")

@pytest.mark.django_db
def test_profile(request):
    # Create some test data
    # test_user = User.objects.create_user(username='test_user')
    # Profile.objects.create(user=test_user)
    user = User.objects.create(
        username="test_user",
        password="testpassword1",
    )
    Profile.objects.create(
        user=user,
        favorite_city="favcity"
    )
    response = client.get(reverse('profile', kwargs={"username": "test_user"}))

    # response = profile(request, username='testuser')
    assertTemplateUsed(response, "profile.html")
    assert 'profile' in response.context
    assert response.context['profile'].user.username == 'test_user'


######## nique sa mère