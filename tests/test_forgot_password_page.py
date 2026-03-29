from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
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


class TestForgotPasswordPage:

    @allure.title("Переход на страницу восстановления пароля со страницы авторизации с проверкой поля ввода почты")
    def test_open_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.go_to_forgot_password()
        forgot_page = ForgotPasswordPage(driver)

        assert forgot_page.is_email_input_visible()      

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_forgot_password_submit_email(self, forgot_password_page):
        forgot_password_page.open()
        forgot_password_page.enter_email("testle@testle.com")
        forgot_password_page.submit()

        assert forgot_password_page.is_password_input_visible()

    @allure.title("Проверка переключателя отображения пароля")
    def test_toggle_password_visibility(self, forgot_password_page):
        forgot_password_page.open()
        forgot_password_page.enter_email("testle@testle.com")
        forgot_password_page.submit()
        forgot_password_page.enter_password("Aa1234567890")

        forgot_password_page.toggle_password_visibility()
        assert forgot_password_page.is_password_visible()
