from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage

from data.urls import Urls
import allure


class ResetPasswordPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("ожидание кнопки Сохранить")
    def wait_save_button(self):
        self.wait_for_element_visible(ResetPasswordPageLocators.SUBMIT_BUTTON)
        self.wait_for_element_clickable(ResetPasswordPageLocators.SUBMIT_BUTTON)

    @allure.step("клик по кнопке показать/скрыть пароль")
    def click_show_password_button(self):
        self.click_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("подсвечивание поля ввода нового пароля")
    def wait_password_buttion_active(self):
        self.wait_for_element_visible(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON_ACTIVE)

    @allure.step("найти подсвеченный элемент")
    def find_field_password_active(self):
        return self.find_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON_ACTIVE)