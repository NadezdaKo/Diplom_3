import allure
from locators.order_feed_locators import OrderFeedLocators
from selenium import webdriver
from .base_page import BasePage
class OrderFeedPage(BasePage):
    @allure.step("Получить счётчик 'Выполнено за всё время'")
    def get_total_completed_orders(self):
        return int(self.get_text_on_element(OrderFeedLocators.TOTAL_COMPLETED))

    @allure.step("Получить счётчик 'Выполнено за сегодня'")
    def get_today_completed_orders(self):
        return int(self.get_text_on_element(OrderFeedLocators.TODAY_COMPLETED))

    @allure.step("Получить номера заказов в работе")
    def get_in_progress_order_number(self):
        self.wait_for_change_text(OrderFeedLocators.IN_PROGRESS_ORDER, "Все текущие заказы готовы!")    
        elements = self.driver.find_elements(OrderFeedLocators.IN_PROGRESS_ORDER[0],OrderFeedLocators.IN_PROGRESS_ORDER[1])
        return [element.text for element in elements]
    
    @allure.step('Дождаться загрузки страницы')
    def order_feed_page_loading_wait(self):
        self.wait_for_element(OrderFeedLocators.IN_PROGRESS_ORDER)