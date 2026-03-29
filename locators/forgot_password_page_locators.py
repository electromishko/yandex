from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    EMAIL_INPUT = By.XPATH, "//input[@name='name']"
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SUBMIT_BUTTON = ("xpath", "//button[text()='Восстановить']")
    CODE_INPUT = ("xpath", "//input[@name='code']")   
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    SHOW_PASSWORD_BUTTON_ACTIVE = (By.XPATH, ".//input[@type='text' and contains(@class, 'text_type_main-default')]")
    SHOW_PASSWORD_BUTTON_DEFAULT = (By.XPATH, ".//input[@type='password' and contains(@class, 'text_type_main-default')]")
