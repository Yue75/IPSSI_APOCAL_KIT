"""Tests pédagogiques pour l'app accounts.

Ces tests servent d'exemples : signup, login, logout, accès protégé.
Lancez : pytest accounts/
"""

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from accounts.models import get_or_create_profile
from quizzes.models import Question, Quiz

pytestmark = pytest.mark.django_db


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def user(db) -> User:
    account = User.objects.create_user(
        username="alice", email="alice@test.com", password="motdepasse123"
    )
    get_or_create_profile(account)
    return account


@pytest.fixture
def quiz(user):
    quiz_obj = Quiz.objects.create(
        user=user,
        title="Quiz de démo",
        source_text="Contenu source",
        score=7,
    )
    Question.objects.create(
        quiz=quiz_obj,
        index=1,
        prompt="Question 1 ?",
        options=["A", "B", "C", "D"],
        correct_index=1,
        selected_index=2,
    )
    return quiz_obj


def test_signup_creates_user(client):
    # Lot 3 : inscription par EMAIL (username = email en interne).
    response = client.post(
        "/api/accounts/signup/",
        {
            "email": "bob@test.com",
            "password": "motdepasse123",
        },
        format="json",
    )
    assert response.status_code == 201, response.data
    assert User.objects.filter(email="bob@test.com").exists()


def test_signup_requires_email(client):
    response = client.post(
        "/api/accounts/signup/",
        {"password": "motdepasse123"},
        format="json",
    )
    assert response.status_code == 400


def test_login_returns_token(client, user):
    response = client.post(
        "/api/accounts/login/",
        {"email": "alice@test.com", "password": "motdepasse123"},
        format="json",
    )
    assert response.status_code == 200, response.data
    assert "token" in response.data
    assert response.data["user"]["email"] == "alice@test.com"


def test_login_with_wrong_password(client, user):
    response = client.post(
        "/api/accounts/login/",
        {"email": "alice@test.com", "password": "wrong"},
        format="json",
    )
    assert response.status_code == 400


def test_me_requires_auth(client):
    response = client.get("/api/accounts/me/")
    assert response.status_code in (401, 403)


def test_me_with_token(client, user):
    from rest_framework.authtoken.models import Token

    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = client.get("/api/accounts/me/")
    assert response.status_code == 200
    assert response.data["username"] == "alice"


def test_logout_invalidates_token(client, user):
    from rest_framework.authtoken.models import Token

    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = client.post("/api/accounts/logout/")
    assert response.status_code == 204
    # Le token n'existe plus
    assert not Token.objects.filter(key=token.key).exists()


def test_export_json(client, user, quiz):
    from rest_framework.authtoken.models import Token

    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = client.get("/api/accounts/me/export/?export_format=json")
    assert response.status_code == 200, response.content
    assert response["Content-Type"].startswith("application/json")
    assert "attachment;" in response["Content-Disposition"]

    payload = response.json()
    assert payload["user"]["email"] == "alice@test.com"
    assert payload["profile"]["email_verified"] is False
    assert len(payload["quizzes"]) == 1
    assert payload["quizzes"][0]["questions"][0]["prompt"] == "Question 1 ?"


def test_export_csv(client, user, quiz):
    from rest_framework.authtoken.models import Token

    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = client.get("/api/accounts/me/export/?export_format=csv")
    assert response.status_code == 200, response.content
    assert response["Content-Type"].startswith("text/csv")

    csv_text = response.content.decode("utf-8")
    assert "entity,id,parent_entity,parent_id,payload_json" in csv_text
    assert "alice@test.com" in csv_text
    assert "Quiz de démo" in csv_text


def test_export_zip(client, user, quiz):
    import json
    import zipfile
    from io import BytesIO

    from rest_framework.authtoken.models import Token

    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = client.get("/api/accounts/me/export/?export_format=zip")
    assert response.status_code == 200, response.content
    assert response["Content-Type"] == "application/zip"

    archive = zipfile.ZipFile(BytesIO(response.content))
    assert set(archive.namelist()) == {
        "manifest.json",
        "user.json",
        "profile.json",
        "quizzes.json",
        "questions.json",
    }
    user_data = json.loads(archive.read("user.json").decode("utf-8"))
    quizzes_data = json.loads(archive.read("quizzes.json").decode("utf-8"))
    assert user_data["email"] == "alice@test.com"
    assert quizzes_data[0]["title"] == "Quiz de démo"


def test_export_rejects_invalid_format(client, user):
    from rest_framework.authtoken.models import Token

    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = client.get("/api/accounts/me/export/?export_format=xml")
    assert response.status_code == 400
