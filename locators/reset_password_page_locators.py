from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    PASSWORD_INPUT = (By.XPATH, ".//input[contains(@class, 'text input') and @type='password' ]")
    SHOW_PASSWORD_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon')]")
    SHOW_PASSWORD_BUTTON_ACTIVE = (By.XPATH, ".//input[@type='text' and contains(@class, 'text_type_main-default')]")
    SHOW_PASSWORD_BUTTON_DEFAULT = (By.XPATH, ".//input[@type='password' and contains(@class, 'text_type_main-default')]")
