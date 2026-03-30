import pytest
from auth.models import User
from django.urls import reverse


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser",
        password="strongpassword",
    )


@pytest.mark.django_db
def test_allow_view_authenticated_user(client, user):
    client.force_login(user)
    response = client.post(reverse("dashboard:dashboard"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_redirect_not_authenticated_user(client):
    response = client.post(reverse("dashboard:dashboard"))
    assert response.status_code == 302
