from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, '"login" is not presented in this URL'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.RIGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(By.CSS_SELECTOR, "input#id_registration-email")
        email_form.send_keys(email)
        pas_form = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
        pas_form.send_keys(password)
        pas_form_two = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
        pas_form_two.send_keys(password)
        button_for_registration = self.browser.find_element(By.CSS_SELECTOR,
                                                            "form#register_form button[value='Register']")
        button_for_registration.click()
