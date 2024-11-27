import allure

import data as d
from locators.login_page_locators import LoginPageLocators
from page_objects.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Open login page")
    def open_login_page(self):
        self.open_url(d.URL.LOGIN_PAGE)
        self.wait_element_visibility_of_element_located(LoginPageLocators.LOG_IN_BUTTON)

    @allure.step("Sign up and login as a new user")
    def log_in(self, registration):
        email, password = registration
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_on_element(LoginPageLocators.LOG_IN_BUTTON)
        self.wait_element_presence_of_element_located(LoginPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Login as an existed user")
    def log_in_main_page(self, registration):
        self.open_login_page()
        self.log_in(registration)

    @allure.step("Login as an existed user and create an order")
    def log_in_with_order(self, log_in_and_create_order):
        email, password, number = log_in_and_create_order
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.wait_element_presence_of_element_located(LoginPageLocators.LOG_IN_BUTTON)
        self.click_on_element(LoginPageLocators.LOG_IN_BUTTON)
        return number

    @allure.step("Click the password reset button")
    def click_recovery_button(self):
        self.click_on_element(LoginPageLocators.RECOVERY_BUTTON)
