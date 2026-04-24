import pytest
import json
from playwright.sync_api import expect

def load_test_data():
    with open('data/login_data.json', encoding='utf-8') as f:
        data = json.load(f)
    # Creamos la lista de datos para la prueba
    cases = [(d['user'], d['pass'], d['msg']) for d in data]
    # Creamos la lista de nombres (IDs) para el reporte
    ids = [d['id'] for d in data]
    return cases, ids

# Cargamos ambos: los casos y sus nombres
cases, test_ids = load_test_data()

@pytest.mark.parametrize("user, password, expected_message", cases, ids=test_ids)
def test_login_saucedemo(login_page, user, password, expected_message):
    login_page.login_to_app(user, password)

    if expected_message is None:
        expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        error_locator = login_page.page.locator("[data-test='error']")
        expect(error_locator).to_contain_text(expected_message)
