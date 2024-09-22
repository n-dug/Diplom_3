import allure
import data as d


class TestMainPage:

    @allure.title('Enter the constructor page')
    def test_check_open_constructor(self, main_page, login_page):
        login_page.open_login_page()
        assert main_page.open_constructor()

    @allure.title('Enter the orders list')
    def test_check_open_order_feed(self, main_page, feed_page):
        main_page.open_main_page()
        assert feed_page.open_order_feed() == d.URL.FEED_PAGE

    @allure.title('Open the ingredients pop up')
    def test_open_pop_up_about_ingredient(self, main_page):
        main_page.open_main_page()
        assert main_page.open_ingredient_pop_up()

    @allure.title('Close the ingredients pop up')
    def test_close_pop_up_about_ingredient(self, main_page):
        main_page.open_main_page()
        main_page.open_ingredient_pop_up()
        assert main_page.close_ingredient_pop_up()

    @allure.title('Assertion of the order created by authorized user')
    def test_check_create_order_authorized_user(self, registration, login_page, main_page):
        login_page.open_login_page()
        login_page.log_in(registration)
        main_page.add_items_in_order()
        assert main_page.create_order_by_click()

    @allure.title('Add an ingredient and check the counter')
    def test_check_counter_up_after_add_item_in_order(self, main_page):
        # The test fails in Firefox. Seems related to the differences in how Firefox and Chrome
        # handle certain elements. This test needs advanced debugging
        main_page.open_main_page()
        counter_1 = main_page.add_items_in_order()
        counter_2 = main_page.check_counter_after_add()
        assert counter_1 == '0', f"Expected initial counter '0', but got '{counter_1}'"
        assert counter_2 == '2', f"Expected updated counter '2', but got '{counter_2}'"
