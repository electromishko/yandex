from locators.history_order_page_locators import HistoryOrderPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators


import time

from pages.base_page import BasePage


class ProfilePage(BasePage):

    def wait_for_profile_load(self):
        self.wait_for_element_visible(ProfilePageLocators.HISTORY_BUTTON)
        return self

    def open_order_history(self):
        self.click_element(ProfilePageLocators.HISTORY_BUTTON)
        from pages.history_order_page import HistoryOrderPage
        history_page = HistoryOrderPage(self.driver)
        history_page.wait_for_page_load()
        return history_page

    def go_to_order_history(self):
        self.click_element(ProfilePageLocators.HISTORY_BUTTON)
        
        from pages.history_order_page import HistoryOrderPage
        history_page = HistoryOrderPage(self.driver)
        history_page.wait_for_page_load()
        return history_page

    def is_order_history_opened(self):
        return self.wait_for_element_present(HistoryOrderPageLocators.ORDERS_HISTORY_CONTENT, timeout=5) is not None

    def logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)
        from pages.login_page import LoginPage
        login_page = LoginPage(self.driver)
        login_page.wait_for_page_load()
        return login_page

    def open(self, user):
        self.driver.get(self.url)
        from pages.main_page import MainPage
        main_page = MainPage(self.driver)
        main_page.login(user)
        main_page.click_account_button()
