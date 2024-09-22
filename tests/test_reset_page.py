import allure

import data as d


class TestRecoveryPassword:

    @allure.title('Assert opening the reset page by clicking the button')
    def test_check_open_recovery_page_on_button(self, login_page):
        # Firefox test fails due to the issue with the modal window that needs advanced debugging
        login_page.open_login_page()
        login_page.click_recovery_button()
        assert login_page.get_current_url() == d.URL.RECOVERY_PAGE

    @allure.title('Assert email input and clicking the reset button')
    def test_enter_email_and_click_recovery_button(self, reset_page, registration):
        reset_page.open_reset_page()
        reset_page.set_email_in_input(registration)
        reset_page.click_recovery_button()
        assert reset_page.get_current_url() == d.URL.RESET_PASSWORD

    @allure.title('Assert clicking the eye icon to make visible the new password')
    def test_check_active_email_input_after_click_eye_icon(self, reset_page, registration):
        reset_page.open_reset_password(registration)
        assert reset_page.click_on_eye_icon()
