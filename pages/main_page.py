from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.main_page_locators import ConstructorPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators

import allure

from selenium.webdriver.support.ui import WebDriverWait


class Tabs:
    BUNS = "buns"
    SAUCES = "sauces"
    FILLINGS = "fillings"


class MainPage(BasePage):

    TAB_LOCATORS = {
        Tabs.BUNS: MainPageLocators.BUN_TAB,
        Tabs.SAUCES: MainPageLocators.SAUCE_TAB,
        Tabs.FILLINGS: MainPageLocators.FILLING_TAB,
    }
   
    def open(self):
        from data.urls import Urls
        self.driver.get(Urls.BASE_URL)

    def open_for_authorized(self):
        self.open()
        self.wait_for_element_visible(MainPageLocators.ORDER_BUTTON)

    def open_for_unauthorized(self):
        self.open()
        self.wait_for_element_visible(MainPageLocators.LOGIN_BUTTON)

    def login(self, user):
        self.click_account_button()
        self.wait_for_element_visible(LoginPageLocators.EMAIL_INPUT)
        self.enter_text(LoginPageLocators.EMAIL_INPUT, user["email"])
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, user["password"])
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

        self.wait_for_element_visible(MainPageLocators.ORDER_BUTTON)

    def is_login_page_opened(self):
        return self.wait_for_element_visible(LoginPageLocators.LOGIN_BUTTON)

    def create_order(self):
        self.add_ingredient("bun")
        self.click_create_order()

        number = self.get_order_number()
        self.close_order_modal()

        return number

    def is_order_success_popup_visible(self):
        return self.wait_for_element_visible(MainPageLocators.ORDER_MODAL)

    def click_logo(self):
        self.click_element(MainPageLocators.LOGO)
        self.wait_for_element_visible(MainPageLocators.ORDER_BUTTON)

    def click_account_button(self):
        self.wait_for_element_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON, timeout=10)
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_constructor_button(self):
        button = self.wait_for_element_clickable(MainPageLocators.CONSTRUCTOR_BUTTON, timeout=10)
        try:
            button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", button)

    def click_feed_button(self):
        button = self.wait_for_element_clickable(MainPageLocators.FEED_LINK, timeout=10)
        try:
            button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", button)
        self.wait_for_element_invisible(MainPageLocators.MODAL_OVERLAY, timeout=10)

    def is_profile_page_opened(self):
        self.wait_for_element_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON, timeout=10)
        return self.wait_for_element_visible(ProfilePageLocators.HISTORY_BUTTON, timeout=5) is not None

    def is_constructor_page_opened(self):
        return self.wait_for_element_visible(ConstructorPageLocators.BURGERS_PAGE)

    @allure.step("Добавление компонента в заказ")
    def add_ingredient(self, ingredient_type):
        mapping = {
            "bun": ConstructorPageLocators.BUN,
            "sauce": ConstructorPageLocators.SAUCE,
            "filling": ConstructorPageLocators.FILLING,
        }
        locator = mapping.get(ingredient_type)

        if not locator:
            raise ValueError(f"Unknown ingredient: {ingredient_type}")

        element = self.wait_for_element_visible(locator)
        self.drag_and_drop(element, ConstructorPageLocators.BASKET)
    

    def add_item_to_constructor(self, item_type):
        if item_type == "bun":
            self.add_bun()
        elif item_type == "sauce":
            self.add_sauce()
        elif item_type == "filling":
            self.add_filling()

    @allure.step("Нажать кнопку Оформить заказ")
    def click_create_order(self):
        self.wait_for_element_invisible(MainPageLocators.MODAL_OVERLAY, timeout=5)
        button = self.wait_for_element_clickable(MainPageLocators.ORDER_BUTTON)
        try:
            button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Нажать кнопку 'Войти в аккаунт' для неавторизованного пользователя")
    def click_create_order_unauthorized(self):
        button = self.wait_for_element_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        try:
            button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Получить номер заказа из модалыного окна")
    def get_order_number(self):
        number_element = self.wait_for_element_visible(
            MainPageLocators.ORDER_NUMBER,
            timeout=15
        )

        WebDriverWait(self.driver, 10).until(
            lambda d: number_element.text.strip() != "9999"
        )

        return number_element.text.lstrip('#').lstrip('0')

    def close_order_modal(self):
        self.wait_for_element_visible(MainPageLocators.MODAL_OVERLAY, timeout=10)
        button = self.wait_for_element_clickable(MainPageLocators.CLOSE_MODAL)
        try:
            button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", button)
        self.wait_for_element_invisible(MainPageLocators.MODAL_OVERLAY, timeout=10)

    def open_tab(self, tab_locator_name):
        tab_locator = getattr(MainPageLocators, tab_locator_name)
        self.click_and_wait_tab_active(tab_locator)

    def is_buns_active(self):
        return self.is_tab_active(MainPageLocators.BUN_TAB)
    
    def is_sauces_active(self):
        return self.is_tab_active(MainPageLocators.SAUCE_TAB)
    
    def is_fillings_active(self):
        return self.is_tab_active(MainPageLocators.FILLING_TAB)
    
    def is_tab_active(self, locator):
        tab = self.wait_for_element_visible(locator, timeout=5)
        class_attr = tab.get_attribute("class")
        return "tab_tab_type_current" in class_attr
    
   
    def go_to_feed(self):
        self.wait_for_page_load(MainPageLocators.FEED_LINK)
        self.driver.find_element(*MainPageLocators.FEED_LINK)
        self.click_feed_button()
        from pages.feed_page import FeedPage
        feed_page = FeedPage(self.driver)
        feed_page.wait_feed_loaded()

        return feed_page
    
    def go_to_profile(self):
        self.click_account_button()

        from pages.profile_page import ProfilePage
        profile_page = ProfilePage(self.driver)
        profile_page.wait_for_profile_load()

        return profile_page
