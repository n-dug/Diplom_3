import pytest
import requests
import allure
from selenium import webdriver

from helpers import Helpers

from data import Ingredients, API
from page_objects.orders_page import OrdersPage
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.account_page import AccountPage
from page_objects.reset_page import ResetPage


@allure.step('Open a new table in Chrome browser. Return the param to the method that called the fixture. '
             'Close this table after finish. Do the same in Firefox')
@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    web_driver.browser_name = request.param
    yield web_driver
    web_driver.quit()


@allure.step('Generate new user data. Send a POST request to create a new user. Get access token from the response.'
             'Send email, password to the method that called the fixture.')
@pytest.fixture(scope='function')
def registration():
    helpers = Helpers()
    email, name, password = helpers.generate_data()
    payload = {
        "email": email,
        "password": password,
        "name": name,
            }
    response = requests.post(API.CREATE_USER, data=payload)
    token = response.json().get("accessToken")
    yield email, password
    requests.delete(API.DELETE_DATA, headers={"Authorization": f'{token}'})


@pytest.fixture(scope='function')
def log_in_and_create_order(registration):
    email, password = registration
    payload = {
        "email": email,
        "password": password,
            }
    response = requests.post(API.LOGIN_USER, data=payload)
    token = response.json().get("accessToken")
    payload = {
        "ingredients": [Ingredients.BUN_CRATOR,
                        Ingredients.FILLING_TETRA,
                        Ingredients.SAUCE_ANTARIAN]
    }
    headers = {"Content-type": "application/json", "Authorization": f'{token}'}
    response = requests.post(API.CREATE_ORDER, headers=headers, json=payload)
    number = str(response.json()['order']['number'])
    return email, password, number


@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='function')
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture(scope='function')
def feed_page(driver):
    return OrdersPage(driver)


@pytest.fixture(scope='function')
def reset_page(driver):
    return ResetPage(driver)
