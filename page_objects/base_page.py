import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from data import global_timeout
from curl import main_site

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие страницы")
    def open(self):
        self.driver.get(f'{main_site}')

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, global_timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Проверка видимости элемента")
    def is_element_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step("Перетащить элемент")
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)
        
    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )
    
    @allure.step("Ожидание изменения текста в элементе")
    def wait_for_change_text(self, locator, text):
        return WebDriverWait(self.driver, global_timeout).until_not(EC.text_to_be_present_in_element(locator,text))