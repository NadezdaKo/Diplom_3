import allure
from locators.main_page_locators import MainPageLocators
from .base_page import BasePage

class MainPage(BasePage):
    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
    
    @allure.step('Дождаться закрытия модального окна')
    def main_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.CLOSE_BUTTON)
        
    @allure.step("Кликнуть на Конструктор")
    def click_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на Ленту заказов")
    def click_order_feed(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT)

    @allure.step("Получить значение счётчика ингредиента")
    def get_counter_value(self):
        counter = self.get_text_on_element(MainPageLocators.INGREDIENT_COUNTER)
        return int(counter) if counter else 0

    @allure.step("Перетащить ингредиент в заказ")
    def drag_ingredient_to_order(self):
        source = self.wait_for_element(MainPageLocators.INGREDIENT)
        target = self.wait_for_element(MainPageLocators.ORDER_DROP_AREA)
        self.drag_and_drop_element(source, target)
        
    @allure.step("Создать заказ")
    def make_order(self):
        self.click_on_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click_on_element(MainPageLocators.CLOSE_BUTTON)
        
    @allure.step("Проверить обновление номера заказа")
    def is_order_number_updated(self):
        return self.wait_for_attribute(MainPageLocators.ORDER_NUMBER)
        
    @allure.step("Получить значение номера заказа")
    def get_order_number(self):
        order_number = self.get_text_on_element(MainPageLocators.ORDER_NUMBER)
        return order_number