import allure
import data as d

from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Open the home page of Stellar Burgers")
    def open_main_page(self):
        self.open_url(d.URL.MAIN_PAGE)
        self.wait_element_visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Open the login page")
    def open_login_account(self):
        self.open_url(d.URL.MAIN_PAGE)
        self.click_on_element(MainPageLocators.ACCOUNT_BUTTON)
        self.wait_element_visibility_of_element_located(MainPageLocators.HEADER_LOGIN_PAGE)

    @allure.step("Open the constructor page")
    def open_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self.find_element(MainPageLocators.HEADER_CONSTRUCTOR)

    @allure.step("Open the pop up window for the ingredients")
    def open_ingredient_pop_up(self):
        self.click_on_element(MainPageLocators.BUN_ITEM)
        self.wait_element_visibility_of_element_located(MainPageLocators.HEADER_POP_UP)
        return self.find_element(MainPageLocators.HEADER_POP_UP)

    @allure.step("Close the pop up window for the ingredients")
    def close_ingredient_pop_up(self):
        self.click_on_element(MainPageLocators.CLOSE_POP_UP_BUTTON)
        self.wait_element_visibility_of_element_located(MainPageLocators.BUN_ITEM)
        return self.find_element(MainPageLocators.CLOSE_POP_UP)

    @allure.step("Add ingredients in an order")
    def add_items_in_order(self):
        self.wait_element_visibility_of_element_located(MainPageLocators.COUNTER_BUN)
        counter = self.get_text(MainPageLocators.COUNTER_BUN)
        self.drag_drop(MainPageLocators.BUN_ITEM, MainPageLocators.ADD_SECTION)
        return counter

    @allure.step("Set a counter after adding ingredients")
    def check_counter_after_add(self):
        counter = self.get_text(MainPageLocators.COUNTER_BUN)
        return counter

    @allure.step("Click a button for order creation")
    def create_order_by_click(self):
        self.wait_element_visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)
        self.wait_element_visibility_of_element_located(MainPageLocators.CREATE_ORDER_POP_UP)
        return self.find_element(MainPageLocators.HEADER_CREATE_ORDER_POP_UP)

    @allure.step("Create order")
    def create_order(self):
        self.open_main_page()
        self.add_items_in_order()
        self.create_order_by_click()
