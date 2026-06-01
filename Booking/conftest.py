import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def api_context():
    with sync_playwright() as p:
        context = p.request.new_context(
            base_url="https://restful-booker.herokuapp.com"
        )
        yield context
        context.dispose()