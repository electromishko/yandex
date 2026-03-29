from selenium.webdriver.common.by import By


class HistoryOrderPageLocators:
    ORDER_LIST = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList')]")
    ORDER_CARD = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList')]//li")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")
    ORDER_MODAL_NUMBER = (By.XPATH,"//div[contains(@class,'Modal_modal__container')]//p[contains(@class,'text_type_digits')]")
    LAST_CARD = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem__')])[last()]")
    FEED_LINK = (By.XPATH, "//a[contains(@href, '/feed')]")
    ORDERS_HISTORY_CONTENT = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]")
    NUMBER_LAST_ORDER_USER = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem__')])[last()]//p[contains(@class, 'text_type_digits-default')]")
    LIST_CARD_ORDER = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]")