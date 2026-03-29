from selenium.webdriver.common.by import By


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]")
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
