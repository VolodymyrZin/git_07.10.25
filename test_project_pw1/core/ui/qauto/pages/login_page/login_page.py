from playwright.sync_api import expect

from test_project_pw1.core.ui.qauto.base_page import BasePage
from test_project_pw1.core.ui.qauto.pages.main_page.main_page import MainPage
from test_project_pw1.core.ui.qauto.pages.registration_page.registration_page import RegistrationPage
from test_project_pw1.core.ui.qauto.pages.registration_page.registration_page_locators import RegistrationPageLocators
from test_project_pw1.core.ui.qauto.pages.login_page.login_page_locators import LoginPageLocators


import logging

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = self.base_url
        self.page_locators = LoginPageLocators()
        self.logger = logging.getLogger('LoginPage')


    def is_page_opened(self)-> bool:
        try:
            expect(self.page.locator(self.page_locators.login_window)).to_be_visible(timeout=5000)
            return True
        except Exception:
            return False




    def click_registration_button(self):
        self.page.locator(self.page_locators.registration_button).click()
        return RegistrationPage(self.page)
