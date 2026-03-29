from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from utils.user_generator import generate_user
from locators.login_page_locators import LoginPageLocators

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


class TestProfilePage:
    @allure.title("Переход в профиль")
    def test_open_profile_page(self, driver, authorized_user):
        main_page = MainPage(driver)

        profile_page = main_page.go_to_profile()

        assert profile_page.wait_for_profile_load() is not None

    @allure.title("Переход в историю заказов")
    def test_go_to_order_history(self, driver, authorized_user):
        main_page = MainPage(driver)

        profile_page = main_page.go_to_profile()
        history_page = profile_page.go_to_order_history()

        assert history_page.wait_for_page_load()

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, authorized_user):
        main_page = MainPage(driver)
        
        profile_page = main_page.go_to_profile()
        login_page = profile_page.logout()

        assert login_page.wait_for_element_visible(LoginPageLocators.EMAIL_INPUT, timeout=10), \
            "Страница логина не загрузилась после выхода"
