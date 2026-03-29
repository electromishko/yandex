from selenium.webdriver.common.by import By


class ProfilePageLocators:
    HISTORY_BUTTON = (By.XPATH, "//a[contains(@href, '/account/profile')]")
    HISTORY_BUTTON = (By.XPATH, "//a[contains(@href, '/account/order-history')]")
    LOGOUT_BUTTON = (By.XPATH, ".//button[@type='button' and text()='Выход']")
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']']")
    CANCEL_BUTTON = (By.XPATH, ".//button[text()='Отмена']']")
