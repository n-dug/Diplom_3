import allure
import data as d

from page_objects.base_page import BasePage
from locators.reset_page_locators import ResetPageLocators


class ResetPage(BasePage):

    @allure.step("Open reset page")
    def open_reset_page(self):
        self.open_url(d.URL.RECOVERY_PAGE)
        self.wait_element_visibility_of_element_located(ResetPageLocators.HEADER_RECOVERY_PAGE)

    @allure.step("Input email")
    def set_email_in_input(self, registration):
        email, _ = registration
        self.send_keys(ResetPageLocators.EMAIL_INPUT, email)

    @allure.step("Click reset button")
    def click_recovery_button(self):
        self.click_on_element(ResetPageLocators.RECOVERY_BUTTON)
        self.wait_element_visibility_of_element_located(ResetPageLocators.SAVE_BUTTON)

    @allure.step("Open the page for creating a new password")
    def open_reset_password(self, registration):
        self.open_reset_page()
        self.set_email_in_input(registration)
        self.click_recovery_button()
        self.send_password(registration)

    @allure.step("Send a new password in input")
    def send_password(self, registration):
        email, _ = registration
        self.send_keys(ResetPageLocators.PASSWORD_INPUT, email)

    @allure.step("Show the password by clicking an eye button")
    def click_on_eye_icon(self):
        self.click_on_element(ResetPageLocators.EYE_BUTTON)
        return self.find_element(ResetPageLocators.PASSWORD_INPUT_ACTIVE)