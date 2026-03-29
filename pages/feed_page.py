from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):

    def wait_feed_loaded(self):
        self.wait_for_element_visible(FeedPageLocators.ORDER_CARD)

    def wait_total_increase(self, old_value):
        self.wait_for_value_increase(self.get_orders_total, old_value)

    def wait_today_increase(self, old_value):
        self.wait_for_value_increase(self.get_today_counter, old_value)

    def get_order_by_number_locator(self, number):
        normalized_number = self.normalize_order_number(number)
        number_with_zero = f"0{normalized_number}"       
        return (
            FeedPageLocators.ORDER_BY_NUMBER[0],
            FeedPageLocators.ORDER_BY_NUMBER[1].format(number=number_with_zero)
        )

    def wait_for_order_in_feed(self, number, timeout=10):
        target = self.normalize_order_number(number)

        def _find(driver):
            cards = driver.find_elements(*FeedPageLocators.ORDER_CARD)

            for card in cards:
                try:
                    raw_text = card.text
                    normalized = self.normalize_order_number(raw_text)

                    if target in normalized:
                        return True
                except:
                    continue
            return False
        try:
            return self.wait_for_function(_find, timeout=timeout)
        except:
            return False
        
    def wait_for_order_in_feed(self, number, timeout=10):
        target = self.normalize_order_number(number)

        def _find(driver):
            cards = driver.find_elements(*FeedPageLocators.ORDER_CARD)

            for card in cards:
                try:
                    raw_text = card.text
                    normalized = self.normalize_order_number(raw_text)

                    if target in normalized:
                        return card
                except Exception:
                    continue

            return False

        return self.wait_for_function(_find, timeout=timeout)

    def is_modal_opened(self):
        return self.wait_for_element_visible(FeedPageLocators.ORDER_MODAL_BOX)

    def get_modal_order_number(self):
        element = self.wait_for_element_visible(FeedPageLocators.ORDER_MODAL_NUMBER, timeout=5)
        return element.text.lstrip('#').lstrip('0')
    

    def open_order_by_number(self, number):
        self.wait_feed_loaded()
        locator = (
            "xpath",
            f"//li[.//p[contains(text(), '{number}')]]"
        )
        card = self.wait_for_element_visible(locator, timeout=10)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", card
        )
        self.wait_for_element_clickable(card)

        try:
            card.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", card)

        self.wait_for_element_visible(
            FeedPageLocators.ORDER_MODAL_NUMBER,
            timeout=10
        )

    def is_order_modal_opened(self, number):
        locator = (
            "xpath",
            f"//div[contains(@class,'Modal')]//p[contains(text(), '{number}')]"
        )
        try:
            self.wait_for_element_visible(locator, timeout=5)
            return True
        except:
            return False
    
    def is_order_present(self, number):
        try:
            self.wait_for_order_in_feed(number, timeout=10)
            return True
        except:
            return False

    def is_order_in_work(self, number, timeout=5):
        return self.wait_for_text(FeedPageLocators.WORK_SECTION, number, timeout)   
    
    def is_order_is_ready(self, number, timeout=60):
        normalized_number = self.normalize_order_number(number)
        number_with_zero = f"0{normalized_number}"
        return self.wait_for_text(FeedPageLocators.READY_SECTION, number_with_zero, timeout)


    def get_orders_total(self):
        value = self.get_element_text(FeedPageLocators.COUNTER_ORDERS_TOTAL)

        return int(value)

    def get_today_counter(self):
        value = self.get_element_text(FeedPageLocators.COUNTER_ORDERS_TODAY)

        return int(value)
