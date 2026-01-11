
from test_project_pw1.utils.settings import d_settings

sign_in_locator = '//*[@class="btn btn-outline-white header_signin"]'

class BasePage:

    def __init__(self, page):
        self.page = page
        self.base_url = d_settings.get("QAUTO_URL", "https://qauto2.forstudy.space/")


    def open_page(self):
        self.page.goto(self.base_url, timeout=5000)

    def click(self, locator:str):
        self.page.click(locator)

    def is_visible(self, locator:str)->bool:
        return self.page.is_visible(locator)

    def fill_field(self, locator: str, text: str):
        self.page.fill(locator, text)



