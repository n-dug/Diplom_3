import allure
import data as d


class TestAccountPage:

    @allure.title('Enter the account from the main page')
    def test_check_enter_to_personal_account_in_main_page(self, main_page):
        main_page.open_login_account()
        assert main_page.get_current_url() == d.URL.LOGIN_PAGE

    @allure.title('Enter the orders list from the account')
    # Firefox test fails due to the issue with the modal window that needs advanced debugging
    def test_check_open_history_orders_in_personal_page(self, registration, login_page, account_page):
        login_page.open_login_page()
        login_page.log_in(registration)
        account_page.open_account_page()
        assert account_page.open_orders_list() == d.URL.HISTORY_PAGE

    @allure.title('Sign out from the account')
    # Firefox test fails due to the issue with the modal window that needs advanced debugging
    def test_check_log_out_account_in_personal_page(self, registration, account_page, login_page):
        login_page.open_login_page()
        login_page.log_in(registration)
        account_page.open_account_page()
        assert account_page.log_out_from_account() == d.URL.LOGIN_PAGE
