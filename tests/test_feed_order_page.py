import pytest
import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.history_order_page import HistoryOrderPage
from pages.register_page import RegisterPage

from utils.user_generator import generate_user


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


class TestFeedOrderPage:

    @allure.title("Заказ проходит полный жизненный цикл: создание → в работе → готов")
    def test_order_lifecycle(self, driver, authorized_user):
        main_page = MainPage(driver)
        number_order = main_page.create_order()
        feed_page = main_page.go_to_feed()

        assert feed_page.is_order_in_work(number_order, timeout=20)
        assert feed_page.is_order_is_ready(number_order, timeout=120)

    @allure.title("Открытие карточки заказа из ленты заказов")
    def test_open_modal_page_order(self, driver, authorized_user):
        main_page = MainPage(driver)
        number = main_page.create_order()
        feed_page = main_page.go_to_feed()
        assert feed_page.wait_for_order_in_feed(number, timeout=10)

        feed_page.open_order_by_number(number)
        assert feed_page.is_modal_opened()

        modal_number = feed_page.get_modal_order_number()
        assert modal_number == number

    @allure.title("Увеличение счётчика заказов за день")
    def test_counter_today_incremented(self, driver, authorized_user):
        main_page = MainPage(driver)
        main_page.create_order()
        feed_page = main_page.go_to_feed()
        before = feed_page.get_today_counter()
        main_page.click_logo()
        main_page.create_order()
        feed_page = main_page.go_to_feed()
        feed_page.wait_today_increase(before)

        assert feed_page.get_today_counter() >= before + 1

    @allure.title("Увеличение счётчика заказов за всё время")
    def test_counter_total_incremented(self, driver, authorized_user):
        main_page = MainPage(driver)

        main_page.create_order()
        feed_page = main_page.go_to_feed()
        before = feed_page.get_orders_total()
        main_page.click_logo()
        main_page.create_order()
        feed_page = main_page.go_to_feed()
        feed_page.wait_total_increase(before)

        assert feed_page.get_orders_total() >= before + 1



    @allure.title("Заказ из истории отображается в ленте")
    def test_show_order_user_in_feed_page(self, driver, authorized_user):
        main_page = MainPage(driver)
        number_order = main_page.create_order()
        profile_page = main_page.go_to_profile()
        profile_page.go_to_order_history()
        history_page = profile_page.go_to_order_history()
        number_history = history_page.get_last_order_number()
        assert number_history == number_order

        main_page.click_logo()
        feed_page = main_page.go_to_feed()
        assert feed_page.wait_for_order_in_feed(number_history, timeout=10)
