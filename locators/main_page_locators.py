from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')
    INGREDIENT = (By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient__1TVf6")]')
    INGREDIENT_COUNTER = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]//p[contains(@class, 'counter')]")
    ORDER_DROP_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    OVERLAY = (By.CLASS_NAME, "Modal_modal__loading__3534A")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")