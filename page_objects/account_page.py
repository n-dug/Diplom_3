import allure

from locators.account_page_locators import AccountPageLocators
from page_objects.base_page import BasePage


class AccountPage(BasePage):

    @allure.step("Open the account")
    def open_account_page(self):
        self.wait_element_visibility_of_element_located(AccountPageLocators.ACCOUNT_BUTTON)
        self.click_on_element(AccountPageLocators.ACCOUNT_BUTTON)

    @allure.step("Open the orders list from the account")
    def open_orders_list(self):
        self.wait_element_visibility_of_element_located(AccountPageLocators.USER_HISTORY_MENU)
        self.click_on_element(AccountPageLocators.USER_HISTORY_MENU)
        return self.get_current_url()

    @allure.step("Find order number in the orders list")
    def find_order_num_in_orders(self):
        self.wait_element_visibility_of_element_located(AccountPageLocators.ORDER_WITH_NUMBER_ORDER_BLOCKS)
        number_in_history = self.get_text(AccountPageLocators.NUMBER_ORDER_BLOCK)
        clean_number_in_history = number_in_history.lstrip('#0')
        return clean_number_in_history

    @allure.step("Log out")
    def log_out_from_account(self):
        self.wait_element_visibility_of_element_located(AccountPageLocators.LOG_OUT_MENU)
        self.click_on_element(AccountPageLocators.LOG_OUT_MENU)
        self.wait_element_visibility_of_element_located(AccountPageLocators.LOG_IN_BUTTON)
        return self.get_current_url()
