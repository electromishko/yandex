from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from utils.user_generator import generate_user

import pytest
import allure


@pytest.fixture
def authorized_user(driver):
    user = generate_user()

    register_page = RegisterPage(driver)
    register_page.open()
    register_page.register(user["name"], user["email"], user["password"])

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(user["email"], user["password"])

    return user


class TestMainPage:

    @allure.title("Переход в профиль по кнопке 'Личный кабинет'")
    def test_open_profile_page(self, driver, authorized_user):
        main_page = MainPage(driver)
        main_page.click_account_button()
        assert main_page.is_profile_page_opened()

    @allure.title("Возврат в конструктор по логотипу")
    def test_return_to_constructor_by_logo(self, driver, authorized_user):
        main_page = MainPage(driver)

        main_page.click_account_button()
        main_page.click_logo()

        assert main_page.is_constructor_page_opened()

    @allure.title("Возврат в конструктор по кнопке 'Конструктор'")
    def test_return_to_constructor_by_button(self, driver, authorized_user):
        main_page = MainPage(driver)

        main_page.click_account_button()
        main_page.click_constructor_button()

        assert main_page.is_constructor_page_opened()

    @allure.title("Переключение на раздел 'Булки'")
    def test_switch_to_buns(self, driver):
        main_page = MainPage(driver)
        main_page.open_tab("SAUCE_TAB")
        main_page.open_tab("BUN_TAB")

        assert main_page.is_buns_active(), "Раздел 'Булки' не активен"
    
    @allure.title("Переключение на раздел 'Соусы'")
    def test_switch_to_sauces(self, driver):
        main_page = MainPage(driver)
        main_page.open_tab("SAUCE_TAB")

        assert main_page.is_sauces_active(), "Раздел 'Соусы' не активен"

    @allure.title("Переключение на раздел 'Начинки'")
    def test_switch_to_fillings(self, driver):
        main_page = MainPage(driver)
        main_page.open_tab("FILLING_TAB")

        assert main_page.is_fillings_active(), "Раздел 'Начинки' не активен"
