import pytest
from auth.models import User
from django.contrib.auth.hashers import check_password
from django.urls import reverse


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser",
        password="strongpassword",
    )


@pytest.mark.django_db
def test_user_valid_login(client, user):
    response = client.post(
        reverse("auth:login"),
        {
            "username": "testuser",
            "password": "strongpassword",
        },
    )
    assert response.status_code == 302


@pytest.mark.django_db
def test_user_invalid_login(client):
    response = client.post(
        reverse("auth:login"),
        {
            "username": "wrongusername",
            "password": "invalidpassword",
        },
    )
    assert "Invalid username or password" in response.text


@pytest.mark.django_db
def test_user_change_password_ok(client, user):
    client.force_login(user)
    client.post(
        reverse("auth:change_password"),
        {
            "old_password": "strongpassword",
            "new_password1": "new_password",
            "new_password2": "new_password",
        },
    )
    user.refresh_from_db()
    assert check_password("new_password", user.password)


@pytest.mark.django_db
def test_user_change_password_not_ok(client, user):
    client.force_login(user)
    client.post(
        reverse("auth:change_password"),
        {
            "old_password": "wrongpassword",
            "new_password1": "new_password",
            "new_password2": "new_password",
        },
    )
    user.refresh_from_db()
    assert not check_password("new_password", user.password)
