from selenium.webdriver.common.by import By

class AuthLocators:
    BUTTON_LOGIN = (By.XPATH, './/button[text() = "Войти в аккаунт"]')
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')
    EMAIL = (By.XPATH, "//input[@name='name' or @type='email']")
    PASSWORD = (By.CSS_SELECTOR, '.input_type_password .input__textfield')
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")