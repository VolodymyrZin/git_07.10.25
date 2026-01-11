
from test_project_pw1.core.ui.qauto.base_page import BasePage
from playwright.sync_api import expect
import logging

from test_project_pw1.core.ui.qauto.pages.registration_page.registration_page_locators import RegistrationPageLocators
from test_project_pw1.tests.ui_tests.qauto_tst.conftest import registering_page


class RegistrationPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = self.base_url
        self.page_locators = RegistrationPageLocators()
        self.logger = logging.getLogger('RegistrationPage')


    def is_page_opened(self):
        return self.is_visible(self.page_locators.registration_locator)

    def is_fields_visible(self):
        expect(self.page.locator(self.page_locators.name_visible_field)).to_be_visible()
        expect(self.page.locator(self.page_locators.last_name_visible_field)).to_be_visible()
        expect(self.page.locator(self.page_locators.email_visible_field)).to_be_visible()
        expect(self.page.locator(self.page_locators.user_pwd_visible_field)).to_be_visible()
        expect(self.page.locator(self.page_locators.user_reenter_pwd_visible_field)).to_be_visible()
        expect(self.page.locator(self.page_locators.registering_button_visible)).to_be_visible()
        return True

    def required_fields(self):

        assert self.page.locator(self.page_locators.user_name).get_attribute('required') is not None
        assert self.page.locator(self.page_locators.last_name).get_attribute('required') is not None
        assert self.page.locator(self.page_locators.email).get_attribute('required') is not None
        assert self.page.locator(self.page_locators.user_pwd).get_attribute('required') is not None
        assert self.page.locator(self.page_locators.user_reenter_pwd).get_attribute('required') is not None

        return True

    def error_message(self):
        self.click(self.page_locators.user_name)
        self.click(self.page_locators.last_name)
        self.click(self.page_locators.email)
        self.click(self.page_locators.user_pwd)
        self.click(self.page_locators.user_reenter_pwd)

        expect(self.page.locator(self.page_locators.name_error_message)).to_be_visible()
        expect(self.page.locator(self.page_locators.last_name_error_message)).to_be_visible()
        expect(self.page.locator(self.page_locators.email_error_message)).to_be_visible()
        expect(self.page.locator(self.page_locators.password_error_message)).to_be_visible()
        expect(self.page.locator(self.page_locators.reenter_password_error_message)).to_be_visible()

    def length_name_symbols_field(self):
        field = self.page.locator(self.page_locators.user_name)
        field.fill('a')
        self.page.locator(self.page_locators.last_name).click()
        expect(self.page.locator(self.page_locators.length_name_not_valid_message)).to_be_visible()

    def digits_in_name_symbols_field(self):
        field = self.page.locator(self.page_locators.user_name)
        field.fill('11111')
        self.page.locator(self.page_locators.last_name).click()
        expect(self.page.locator(self.page_locators.symbols_name_not_valid_message)).to_be_visible()

    def is_passwords_identical(self):
        field1 = self.page.locator(self.page_locators.user_pwd)
        field2 = self.page.locator(self.page_locators.user_reenter_pwd)
        field1.fill('Password123!')
        field2.fill('Password1234!')
        self.page.locator('body').click()
        expect(self.page.locator(self.page_locators.password_identically_message)).to_be_visible()
