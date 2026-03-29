from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from data.urls import Urls

class ForgotPasswordPage(BasePage):

    def open(self):
        self.driver.get(Urls.FORGOT_PASSWORD)
        self.wait_for_element_visible(ForgotPasswordPageLocators.EMAIL_INPUT)

    def enter_email(self, email):
        self.wait_for_element_visible(ForgotPasswordPageLocators.EMAIL_INPUT).send_keys(email)

    def is_code_input_visible(self):
        return self.wait_for_element_visible(ForgotPasswordPageLocators.CODE_INPUT)

    def enter_password(self, password):
        self.enter_text(ForgotPasswordPageLocators.PASSWORD_INPUT, password)

    def is_password_visible(self):
        field = self.wait_for_element_visible(ForgotPasswordPageLocators.PASSWORD_INPUT)
        return field.get_attribute("type") == "text"
    
    def is_password_input_visible(self):
        return self.wait_for_element_visible(ForgotPasswordPageLocators.PASSWORD_INPUT)
    
    def is_email_input_visible(self):
        return self.wait_for_element_visible(ForgotPasswordPageLocators.EMAIL_INPUT)
       
    def toggle_password_visibility(self):
        button = self.wait_for_element_clickable(ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON, timeout=5)
        try:
            button.click()
        except:
            self.driver.execute_script("arguments[0].click();", button)
        return self

    def submit(self):
        self.wait_for_element_invisible(ForgotPasswordPageLocators.MODAL_OVERLAY, timeout=5)
        button = self.wait_for_element_clickable(ForgotPasswordPageLocators.SUBMIT_BUTTON)
        try:
            button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", button)
