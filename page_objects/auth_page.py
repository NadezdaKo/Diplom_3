import allure
from locators.auth_locators import AuthLocators
from .base_page import BasePage

class AuthPage(BasePage):
    @allure.step("Авторизоваться")
    def auth(self, email, password):
        self.click_on_element(AuthLocators.BUTTON_LOGIN)
        self.send_keys_to_input(AuthLocators.EMAIL, email)
        self.send_keys_to_input(AuthLocators.PASSWORD, password)
        self.click_on_element(AuthLocators.LOGIN_BUTTON)