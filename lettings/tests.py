# import unittest
#
# from django.urls import reverse
#
# from .models import Letting
# from django.test import RequestFactory, Client, TestCase
#
#
# class TestLetting(TestCase):
#     client = Client()
#
#     def test_lettings(self):
#         # Call the method under test by generating the URL using the reverse function
#         response = self.client.get(reverse('lettings_index'))
#
#         # Assert that the response has a 200 status code
#         self.assertEqual(response.status_code, 200)
#
#         # Assert that the correct template was used to render the response
#         self.assertTemplateUsed(response, 'lettings_index.html')
#
#     def test_letting(self):
#         # Call the method under test by generating the URL using the reverse function
#         response = self.client.get(reverse('letting', kwargs={'letting_id': self.client}))
#
#         # Assert that the response has a 200 status code
#         self.assertEqual(response.status_code, 200)
#
#         # Assert that the correct template was used to render the response
#         self.assertTemplateUsed(response, 'letting.html')
#
#         # Check that the correct letting was passed to the template
#         # self.assertEqual(self.letting.title, response.context['title'])
#         # self.assertEqual(self.letting.address, response.context['address'])
#         self.assertIn(b'<title>Oceanview Retreat</title>', response.content)
#
import pytest
from django.urls import reverse
from django.test import Client

from .models import Letting, Address

client = Client()

@pytest.mark.django_db
def test_lettings_index(client):
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200
    assert 'lettings_list' in response.context
#
@pytest.mark.django_db
def test_letting(client):

    Address.objects.create(number=321,
        street=' B street',
        city="Z city",
        state=" C state",
        zip_code=88000,
        country_iso_code="FR-fr")

    address = Address.objects.all()[0]

    letting = Letting.objects.create(
        title='The test title',
        address= address,
    )
    print(letting)
    response = client.get(reverse('letting', kwargs={'letting_id': 1}))
#         response = self.client.get(reverse('letting', kwargs={'letting_id': self.client}))

    assert response.status_code == 200
    assert response.context['title'] == letting.title
    assert response.context['address'] == letting.address
