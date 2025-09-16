from selenium.webdriver.common.by import By

class IngredientLocators:
    MODAL = (By.XPATH, "//div[contains(@class, 'modal')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")