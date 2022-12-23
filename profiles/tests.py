import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from .models import Profile
from pytest_django.asserts import assertTemplateUsed

client = Client()


@pytest.mark.django_db
def test_profiles_index(request):

    response = client.get(reverse("profiles_index"))

    assert response.status_code == 200
    assert "profiles_list" in response.context
    assertTemplateUsed(response, "profiles_index.html")


@pytest.mark.django_db
def test_profile(request):

    user = User.objects.create(
        username="test_user",
        password="testpassword1",
    )
    Profile.objects.create(user=user, favorite_city="favcity")
    response = client.get(reverse("profile", kwargs={"username": "test_user"}))
    assertTemplateUsed(response, "profile.html")
    assert "profile" in response.context
    assert response.context["profile"].user.username == "test_user"
