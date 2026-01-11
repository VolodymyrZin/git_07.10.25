
from test_project_pw1.core.ui.qauto.base_page import BasePage
from playwright.sync_api import expect

class MainPage(BasePage):

    page_title_locator = "//*[@class='section contacts']//h2['_ngcontent-ixu-c64']"


    def __init__(self, page):
        super().__init__(page)
        self.url = f'{self.base_url}'

    def is_page_opened(self):
        check_1 = self.page.url.startswith(self.base_url)
        try:
            expect(self.page.locator(self.page_title_locator)
                   ).to_have_text('Contacts', timeout=2000)

            if check_1 is True:
                return True
            else:
                return False

        except Exception:
            return False

    sign_in_locator = '//*[@class="btn btn-outline-white header_signin"]'

    def click_sign_in(self):
        from test_project_pw1.core.ui.qauto.pages.login_page.login_page import LoginPage
        self.click(self.sign_in_locator)   # метод з BasePage
        return LoginPage(self.page)



