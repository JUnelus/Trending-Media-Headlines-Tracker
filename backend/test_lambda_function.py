import pytest
from lambda_function import lambda_handler

def test_lambda_handler_success(mocker):
    mocker.patch('requests.get', return_value=MockResponse())
    event = {}
    response = lambda_handler(event, None)
    assert response['statusCode'] == 200

class MockResponse:
    def json(self):
        return {
            "articles": [
                {"title": "Headline 1"},
                {"title": "Headline 2"},
                {"title": "Headline 3"},
                {"title": "Headline 4"},
                {"title": "Headline 5"}
            ]
        }
