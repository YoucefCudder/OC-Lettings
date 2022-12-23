import pytest
from django.urls import reverse
from django.test import Client
from .models import Letting, Address

client = Client()


@pytest.mark.django_db
def test_lettings_index(client):
    response = client.get(reverse("lettings_index"))
    assert response.status_code == 200
    assert "lettings_list" in response.context


#
@pytest.mark.django_db
def test_letting(client):

    Address.objects.create(
        number=321,
        street=" B street",
        city="Z city",
        state=" C state",
        zip_code=88000,
        country_iso_code="FR-fr",
    )

    address = Address.objects.all()[0]

    letting = Letting.objects.create(
        title="The test title",
        address=address,
    )
    print(letting)
    response = client.get(reverse("letting", kwargs={"letting_id": 1}))

    assert response.status_code == 200
    assert response.context["title"] == letting.title
    assert response.context["address"] == letting.address
