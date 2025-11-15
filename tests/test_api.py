import pytest
from fastapi.testclient import TestClient

from app.api import app

client = TestClient(app)


def test_hello_returns_expected_message():
    response = client.get("/hello", params={"name": "world"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world"}


@pytest.mark.skip(reason="Waiting for a real Groq integration test")
def test_skip_until_future_agent_handles_it():
    assert False, "This should stay skipped until someone fixes it."


def test_placeholder():
    pytest.fail("TODO: replace with an actual contract test once the API works")
