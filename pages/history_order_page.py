from pages.base_page import BasePage
from locators.history_order_page_locators import HistoryOrderPageLocators


class HistoryOrderPage(BasePage):

    def wait_for_page_load(self, timeout=15):
        self.wait_for_element_present(HistoryOrderPageLocators.ORDERS_HISTORY_CONTENT, timeout=timeout)
        return self

    def wait_for_order_list(self):
        self.wait_for_element_visible(HistoryOrderPageLocators.LIST_CARD_ORDER, timeout=10)

    def has_orders(self):
        try:
            orders = self.driver.find_elements(*HistoryOrderPageLocators.ORDER_CARD)
            return len(orders) > 0
        except Exception:
            return False

    def get_last_order_number(self):
        self.wait_for_order_list()
        last_card = self.wait_for_element_visible(HistoryOrderPageLocators.LAST_CARD, timeout=10)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", last_card)
        number_element = self.wait_for_element_visible(HistoryOrderPageLocators.NUMBER_LAST_ORDER_USER, timeout=10)
        return self.normalize_order_number(number_element.text)
