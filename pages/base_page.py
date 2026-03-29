from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:

    default_timeout = 10

    TAB_ACTIVE_CLASS = "tab_tab_type_current"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_until(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)

    def wait_for_element_visible(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.default_timeout).until(
            EC.visibility_of_element_located(locator))
    
    def wait_for_element_invisible(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.default_timeout).until(EC.invisibility_of_element_located(locator))

    def wait_for_value_increase(self, get_value_func, old_value, timeout=None):
        WebDriverWait(self.driver, timeout or self.default_timeout).until(lambda d: get_value_func() > old_value)

    def wait_for_element_clickable(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.default_timeout).until(EC.element_to_be_clickable(locator))
     
    def wait_for_text(self, locator, text, timeout=None):
        return WebDriverWait(self.driver, timeout or self.default_timeout).until(
                lambda driver: text in driver.find_element(*locator).text)

    def wait_for_function(self, func, timeout=None, poll=0.1):
        return WebDriverWait(self.driver, timeout or self.default_timeout, poll_frequency=poll).until(func)

    def wait_for_order_in_feed(self, number, timeout=15):
        target = self.normalize_order_number(number)

        def _find(driver):
            elements = driver.find_elements(
                "xpath",
                "//p[contains(@class,'text_type_digits')]"
            )

            normalized_numbers = []

            for el in elements:
                try:
                    normalized = self.normalize_order_number(el.text)
                    normalized_numbers.append(normalized)
                except:
                    continue

            return target in normalized_numbers
        try:
            return self.wait_for_function(_find, timeout=timeout)
        except:
            return False

    def wait_for_page_load(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))
    

    def wait_for_element_has_class(self, locator, class_name, timeout=10):
        self.wait_until(
            lambda d: class_name in d.find_element(*locator).get_attribute("class"),
            timeout
        )

    def wait_for_element_present(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.default_timeout).until(
            EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=None):
        element = self.wait_for_element_clickable(locator, timeout)
        browser_name = self.driver.capabilities.get('browserName', '').lower()
        
        if browser_name == 'firefox':
            try:
                ActionChains(self.driver).move_to_element(element).click().perform()
                return
            except ElementClickInterceptedException:
                pass
        try:
            element.click()
            return
        except ElementClickInterceptedException:
            pass
        self.driver.execute_script("arguments[0].click();", element)

    def click_and_wait_tab_active(self, locator, timeout=10):
        tab = self.wait_for_element_clickable(locator, timeout)
        try:
            tab.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", tab)

        self.wait_until(
            lambda d: self.TAB_ACTIVE_CLASS in tab.get_attribute("class"),
            timeout
        )

    def enter_text(self, locator, text, timeout=None):
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator, timeout=None):
        element = self.wait_for_element_visible(locator, timeout)
        return element.text

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_counter_increase(feed_page, old_value):
        WebDriverWait(feed_page.driver, 10).until(
            lambda d: int(feed_page.get_orders_total()) > old_value)

    def drag_and_drop(self, source, target_locator):
        target = self.wait_for_element_visible(target_locator)

        self.driver.execute_script("""
            function triggerDragAndDrop(source, target) {
                const dataTransfer = new DataTransfer();

                function fireEvent(type, elem) {
                    const event = new DragEvent(type, {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    elem.dispatchEvent(event);
                }

                fireEvent('dragstart', source);
                fireEvent('dragenter', target);
                fireEvent('dragover', target);
                fireEvent('drop', target);
                fireEvent('dragend', source);
            }

            triggerDragAndDrop(arguments[0], arguments[1]);
        """, source, target)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def is_tab_active(self, locator):
        tab = self.wait_for_element_visible(locator)
        class_attr = tab.get_attribute("class")
        return "tab_tab_type_current" in class_attr

    @staticmethod
    def normalize_order_number(input):
        return input.lstrip('#').lstrip('0')
