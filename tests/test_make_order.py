

from pages.register_page import RegisterPage
from pages.login_page import LoginPage
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


class TestMakeOrder:
    @allure.title("Заказ авторизованного пользователя")
    def test_make_order_authorized_user(self, main_page, authorized_user):
        main_page.open_for_authorized()
        order_number = main_page.create_order()
        assert order_number is not None

    @allure.title("У неавторизованного пользователя отображается кнопка авторизации")
    def test_make_order_unauthorized_user(self, main_page):
        main_page.open_for_unauthorized()
        main_page.add_ingredient("bun")
        main_page.click_create_order_unauthorized()

        assert main_page.is_login_page_opened()
