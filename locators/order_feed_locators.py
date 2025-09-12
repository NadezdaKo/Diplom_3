from selenium.webdriver.common.by import By

class OrderFeedLocators:
    TOTAL_COMPLETED = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    TODAY_COMPLETED = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    IN_PROGRESS_ORDER = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')
    OVERLAY = (By.CLASS_NAME, "Modal_modal__loading__3534A")