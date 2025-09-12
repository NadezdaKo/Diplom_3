import allure
from page_objects.main_page import MainPage
from page_objects.order_feed_page import OrderFeedPage

class TestOrderFeed:
    @allure.title("Увеличение счётчика 'Выполнено за всё время'")
    def test_total_completed_orders_increase(self, login):
        driver = login
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        order_feed = OrderFeedPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_order_feed()
        order_feed.order_feed_page_loading_wait()
        initial_count = order_feed.get_total_completed_orders()
        main_page.click_constructor()
        main_page.main_page_loading_wait()
        main_page.drag_ingredient_to_order()
        main_page.make_order()
        main_page.main_page_loading_wait()
        main_page.close_modal()
        main_page.main_loading_wait()
        main_page.click_order_feed()
        order_feed.order_feed_page_loading_wait()
        new_count = order_feed.get_total_completed_orders()
        assert new_count > initial_count

    @allure.title("Увеличение счётчика 'Выполнено за сегодня'")
    def test_today_completed_orders_increase(self, login):
        driver = login
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        order_feed = OrderFeedPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_order_feed()
        order_feed.order_feed_page_loading_wait()
        initial_count = order_feed.get_today_completed_orders()
        main_page.click_constructor()
        main_page.main_page_loading_wait()
        main_page.drag_ingredient_to_order()
        main_page.make_order()
        main_page.main_page_loading_wait()
        main_page.close_modal()
        main_page.main_loading_wait()
        main_page.click_order_feed()
        order_feed.order_feed_page_loading_wait()
        main_page.main_page_loading_wait()
        new_count = order_feed.get_today_completed_orders()
        assert new_count > initial_count

    @allure.title("Появление номера заказа в 'В работе'")
    def test_order_in_progress(self, login):
        driver = login
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_constructor()
        main_page.main_page_loading_wait()
        main_page.drag_ingredient_to_order()
        main_page.make_order()
        main_page.main_page_loading_wait()
        order_number = '0' + main_page.get_order_number()
        main_page.main_page_loading_wait()
        main_page.close_modal()
        main_page.main_loading_wait()
        main_page.main_page_loading_wait()
        main_page.click_order_feed()
        order_feed.order_feed_page_loading_wait()
        assert order_number in order_feed.get_in_progress_order_number()