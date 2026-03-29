from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators
from data.urls import Urls


class RegisterPage(BasePage):

    def open(self):
        from pages.main_page import MainPage      
        main_page = MainPage(self.driver)
        main_page.click_account_button()
        self.click_register_link()
        
        return self

    def open_via_url(self):

        self.navigate(Urls.REGISTER)
        self.wait_for_element_visible(RegisterPageLocators.NAME_INPUT)
        return self

    def click_register_link(self):
        self.click_element(RegisterPageLocators.REGISTER_LINK)
        self.wait_for_element_visible(RegisterPageLocators.NAME_INPUT)
        return self

    def register(self, name, email, password):
        self.wait_for_element_visible(RegisterPageLocators.NAME_INPUT)
        self.enter_text(RegisterPageLocators.NAME_INPUT, name)
        self.enter_text(RegisterPageLocators.EMAIL_INPUT, email)
        self.enter_text(RegisterPageLocators.PASSWORD_INPUT, password)
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)
        
        from pages.login_page import LoginPage
        login_page = LoginPage(self.driver)
        login_page.wait_for_page_load()
        
        return login_page

    def enter_name(self, name):
        self.enter_text(RegisterPageLocators.NAME_INPUT, name)
        return self

    def enter_email(self, email):
        self.enter_text(RegisterPageLocators.EMAIL_INPUT, email)
        return self

    def enter_password(self, password):
        self.enter_text(RegisterPageLocators.PASSWORD_INPUT, password)
        return self

    def click_register_button(self):
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)
        return self

    def wait_for_page_load(self, timeout=10):
        self.wait_for_element_visible(RegisterPageLocators.NAME_INPUT, timeout=timeout)
        return self
