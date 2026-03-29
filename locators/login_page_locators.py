from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]')
    EMAIL_INPUT = By.XPATH, "//input[@name='name']"
    PASSWORD_INPUT = By.XPATH, "//input[@name='Пароль']"  
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
    