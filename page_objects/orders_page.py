import allure
import data as d

from locators.orders_page_locators import OrdersPageLocators
from page_objects.base_page import BasePage


class OrdersPage(BasePage):

    @allure.step("Open orders page")
    def open_feed_page(self):
        self.open_url(d.URL.FEED_PAGE)
        self.wait_element_visibility_of_element_located(OrdersPageLocators.HEADER_ORDER_FEED)

    @allure.step("Open orders list")
    def open_order_feed(self):
        self.click_on_element(OrdersPageLocators.ORDER_FEED_BUTTON)
        self.wait_element_visibility_of_element_located(OrdersPageLocators.HEADER_ORDER_FEED)
        self.find_element(OrdersPageLocators.HEADER_ORDER_FEED)
        return self.get_current_url()

    @allure.step("Check all time counter")
    def check_counter_all_time(self):
        self.wait_element_visibility_of_element_located(OrdersPageLocators.COUNTER_ALL_TIME)
        counter = self.find_element(OrdersPageLocators.COUNTER_ALL_TIME)
        return counter.text

    @allure.step("Check today counter")
    def check_counter_day(self):
        self.wait_element_visibility_of_element_located(OrdersPageLocators.COUNTER_DAY)
        counter = self.find_element(OrdersPageLocators.COUNTER_DAY)
        return counter.text

    @allure.step("Check order number in orders list")
    def check_number_order_in_feed_page(self, number):
        orders = self.find_all_element(OrdersPageLocators.ORDER_WITH_NUMBER_ORDER_BLOCKS)
        for _ in orders:
            if number in _.text:
                return True
        return False

    @allure.step("Click orders block")
    def click_on_order_block(self):
        self.click_on_element(OrdersPageLocators.ORDER_BLOCK)
        self.wait_element_visibility_of_element_located(OrdersPageLocators.ORDER_BLOCK_POP_UP)
        return self.find_element(OrdersPageLocators.NUMBER_ORDER_BLOCK)

    @allure.step("Check that order is being processed")
    def check_number_order_in_at_work(self):
        self.wait_element_visibility_of_element_located(OrdersPageLocators.NUMBER_ORDER_LIST_ONLINE)
        counter = self.find_element(OrdersPageLocators.NUMBER_ORDER_LIST_ONLINE)
        # delete the 1st zero of order's number and return it
        return counter.text.lstrip('0')
