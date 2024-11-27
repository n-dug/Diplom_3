import allure


class TestFeedOrdersPage:

    @allure.title('Assert opening orders details by clicking on its block')
    def test_check_open_order_details(self, feed_page):
        feed_page.open_feed_page()
        assert feed_page.click_on_order_block()

    @allure.title('Synchronisation of content in all orders list and recent orders (feed)')
    def test_check_sync_history_order_and_feed_orders(self, feed_page, log_in_and_create_order,
                                                      login_page, account_page):
        # Firefox test fails due to the issue with the modal window that needs advanced debugging
        # Also Chrome test fails sometimes due to TimeoutException that is hard to handle
        login_page.open_login_page()
        number = login_page.log_in_with_order(log_in_and_create_order)
        account_page.open_account_page()
        account_page.open_orders_list()
        number_in_history = account_page.find_order_num_in_orders()
        feed_page.open_feed_page()
        number_in_feed = feed_page.check_number_order_in_feed_page(number)
        assert number == number_in_history and number_in_feed is True

    @allure.title('Check that the all time counter increases after creating new order')
    def test_check_rise_counter_all_time_after_made_order(self, feed_page, login_page, main_page, registration):
        # Firefox test fails due to the issue with the modal window that needs advanced debugging
        feed_page.open_feed_page()
        counter_before = feed_page.check_counter_all_time()
        login_page.log_in_main_page(registration)
        main_page.create_order()
        feed_page.open_feed_page()
        counter_after = feed_page.check_counter_all_time()
        assert counter_before != counter_after

    @allure.title('Check that the processing counter increases after creating new order')
    def test_check_rise_counter_at_work_after_made_order(self, feed_page, login_page, account_page, main_page,
                                                         registration, log_in_and_create_order):
        # The test fails in Firefox. Seems related to the differences in how Firefox and Chrome
        # handle certain elements. This test needs advanced debugging
        login_page.open_login_page()
        number = login_page.log_in_with_order(log_in_and_create_order)
        feed_page.open_feed_page()
        number_in_at_work = feed_page.check_number_order_in_at_work()
        assert number == number_in_at_work

    @allure.title('Check that the today counter increases after creating new order')
    def test_check_rise_counter_day_after_made_order(self, feed_page, login_page, main_page, registration):
        # Firefox test fails due to the issue with the modal window that needs advanced debugging
        feed_page.open_feed_page()
        counter_before = feed_page.check_counter_day()
        login_page.log_in_main_page(registration)
        main_page.create_order()
        feed_page.open_feed_page()
        counter_after = feed_page.check_counter_day()
        assert counter_before != counter_after
