import allure
from locators.ingredient_locators import IngredientLocators
from .base_page import BasePage

class IngredientDetailsPage(BasePage):
    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        return self.is_element_displayed(IngredientLocators.MODAL)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click_on_element(IngredientLocators.CLOSE_BUTTON)
        self.wait_for_element_hide(IngredientLocators.MODAL)