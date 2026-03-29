from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data.urls import Urls


class LoginPage(BasePage):

    def open(self):
        from pages.main_page import MainPage
        
        main_page = MainPage(self.driver)
        main_page.click_account_button()
        self.wait_for_element_visible(LoginPageLocators.EMAIL_INPUT)
        return self

    def open_via_url(self):
        self.navigate(Urls.LOGIN)
        self.wait_for_element_visible(LoginPageLocators.EMAIL_INPUT)

    def login(self, email, password):
        self.wait_for_element_visible(LoginPageLocators.EMAIL_INPUT)
        self.enter_text(LoginPageLocators.EMAIL_INPUT, email)
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        
        from locators.main_page_locators import MainPageLocators
        self.wait_for_element_visible(MainPageLocators.ORDER_BUTTON)
        
        from pages.main_page import MainPage
        return MainPage(self.driver)

    def enter_email(self, email):
        self.wait_for_element_visible(LoginPageLocators.EMAIL_INPUT)
        self.enter_text(LoginPageLocators.EMAIL_INPUT, email)
        return self

    def enter_password(self, password):
        self.wait_for_element_visible(LoginPageLocators.PASSWORD_INPUT)
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)
        return self

    def go_to_forgot_password(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON)

    def wait_for_page_load(self, timeout=10):
        self.wait_for_element_visible(LoginPageLocators.EMAIL_INPUT, timeout=timeout)
        return self
