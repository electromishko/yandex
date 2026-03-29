from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDER_CARD = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList')]//li")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")
    ORDER_MODAL_BOX = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]")
    ORDER_MODAL_NUMBER = (By.XPATH,"//div[contains(@class,'Modal_modal__container')]//p[contains(@class,'text_type_digits')]")
    ORDER_LIST = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList')]")
    COUNTER_ORDERS_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    COUNTER_ORDERS_TOTAL = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    ORDER_BY_NUMBER = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList')]//li[.//p[contains(text(), '{number}')]]")
    WORK_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")   
    READY_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList__')]")
