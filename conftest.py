import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    return login