import pytest
from django.urls import reverse
from django.conf import settings


@pytest.mark.django_db
def test_fetch_todos_unauthenticated_returns_error(client):
    """ Make sure that we get Authentication error response if we have no todos created """
    response = client.get(reverse("todo-list"))
    data = response.json()
    print("test data ", data)
    assert {"detail": "Authentication credentials were not provided."} == data
