import allure
from page_objects.main_page import MainPage
from page_objects.ingredient_details_page import IngredientDetailsPage
from curl import main_site

class TestMainFunctionality:
    @allure.title("Переход по клику на Конструктор")
    def test_click_constructor(self, login):
        main_page = MainPage(login)
        main_page.open()
        main_page.main_page_loading_wait()
        main_page.click_order_feed()
        main_page.click_constructor()
        assert login.current_url == main_site

    @allure.title("Переход по клику на Ленту заказов")
    def test_click_order_feed(self, login):
        main_page = MainPage(login)
        main_page.open()
        main_page.main_page_loading_wait()
        main_page.click_order_feed()
        assert "/feed" in login.current_url

    @allure.title("Открытие деталей ингредиента")
    def test_ingredient_details_modal(self, login):
        main_page = MainPage(login)
        main_page.open()
        main_page.main_page_loading_wait()
        main_page.click_ingredient()
        details_page = IngredientDetailsPage(login)
        assert details_page.is_modal_visible()

    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, login):
        main_page = MainPage(login)
        main_page.open()
        main_page.main_page_loading_wait()
        main_page.click_ingredient()
        details_page = IngredientDetailsPage(login)
        details_page.close_modal()
        assert not details_page.is_modal_visible()

    @allure.title("Увеличение счётчика ингредиента")
    def test_ingredient_counter_increase(self, login):
        main_page = MainPage(login)
        main_page.open()
        main_page.main_page_loading_wait()
        initial_count = main_page.get_counter_value()
        main_page.drag_ingredient_to_order()
        new_count = main_page.get_counter_value()
        assert new_count == initial_count + 2