import pytest

from test_project_pw1.core.ui.qauto.pages.login_page.login_page import LoginPage
from test_project_pw1.tests.ui_tests.qauto_tst.conftest import RegisteringSuite
from test_project_pw1.utils.settings import d_settings
from test_project_pw1.core.ui.qauto.pages.main_page.main_page import MainPage
from playwright.sync_api import sync_playwright, expect
from allure_commons.types import LinkType
from definitions import BASE_PATH
import time
import pathlib
import allure


# шлях до кореня проєкту
# BASE_PATH = pathlib.Path(__file__).parent

@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("Main Page")
class TestMainPage(RegisteringSuite):
    @allure.link('jira.com/bug-123', link_type=LinkType.ISSUE)
    @allure.link('jira.com/feature-345', link_type=LinkType.TEST_CASE)
    @allure.description('Just base check for opening main page')
    @allure.story("Smoke check")
    @allure.title("Головна сторінка відкривається")
    def test_smoke_main_page(self, pw_page, main_page):
        assert main_page.is_page_opened() is True, 'Home page was\'nt opened'
        pw_page.wait_for_timeout(1000)


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Login")
class TestLogin(RegisteringSuite):
    @allure.story("Login modal")
    @allure.title("Модальне вікно логіну відкривається")
    def test_login_modal(self, pw_page, main_page):
        login_page = main_page.click_sign_in()
        assert login_page.is_page_opened(), "Login modal wasn't opened"
        pw_page.wait_for_timeout(1000)


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Register")
class TestRegistering(RegisteringSuite):
    @allure.story("Registration modal")
    @allure.title("Модальне вікно реєстрації відкривається")
    def test_register_modal(self, pw_page, main_page):
        with allure.step("Відкрити модальне вікно логіну"):
            login_page = main_page.click_sign_in()
            assert login_page.is_page_opened(), "Login modal wasn't opened"

        with allure.step("Відкрити модальне вікно реєстрації"):
            registering_page = login_page.click_registration_button()
            assert registering_page.is_page_opened(), "Registration modal wasn't opened"

        pw_page.wait_for_timeout(1000)

    @allure.story("Fields visibility")
    @allure.title("Всі поля реєстрації видимі")
    def test_is_fields_visible(self, pw_page, main_page):
        with allure.step("Відкрити сторінку реєстрації"):
            login_page = main_page.click_sign_in()
            registering_page = login_page.click_registration_button()

        with allure.step("Перевірити видимість полів"):
            assert registering_page.is_fields_visible(), "Fields are not visible"

        pw_page.wait_for_timeout(1000)

    @allure.story("Required fields validation")
    @allure.title("Перевірка обов'язкових полів")
    def test_required_fields(self, pw_page, registering_page):
        fields = [
            registering_page.page.locator(registering_page.page_locators.user_name),
            registering_page.page.locator(registering_page.page_locators.last_name),
            registering_page.page.locator(registering_page.page_locators.email),
            registering_page.page.locator(registering_page.page_locators.user_pwd),
            registering_page.page.locator(registering_page.page_locators.user_reenter_pwd),
        ]

        error_messages = [
            registering_page.page.locator(registering_page.page_locators.name_error_message),
            registering_page.page.locator(registering_page.page_locators.last_name_error_message),
            registering_page.page.locator(registering_page.page_locators.email_error_message),
            registering_page.page.locator(registering_page.page_locators.password_error_message),
            registering_page.page.locator(registering_page.page_locators.reenter_password_error_message),
        ]

        for i, (field, error) in enumerate(zip(fields, error_messages)):
            field.click()
            if i < len(fields) - 1:
                fields[i + 1].click()
            else:
                registering_page.page.locator("body").click()
            expect(error).to_be_visible()
        pw_page.wait_for_timeout(1000)

    @allure.story("Register button state")
    @allure.title("Кнопка реєстрації активується після заповнення")
    def test_register_button_enabled(self, pw_page, registering_page):
        button = registering_page.page.locator(registering_page.page_locators.registering_button)
        with allure.step('Перевірити, що кнопка спочатку неактивна'):
            expect(button).to_be_disabled()

        with allure.step('Заповнити всі поля'):
            registering_page.page.fill(registering_page.page_locators.user_name, "Test")
            registering_page.page.fill(registering_page.page_locators.last_name, "User")
            registering_page.page.fill(registering_page.page_locators.email, "testuser@example.com")
            registering_page.page.fill(registering_page.page_locators.user_pwd, "Password123!")
            registering_page.page.fill(registering_page.page_locators.user_reenter_pwd, "Password123!")

        with allure.step('Перевірити, що кнопка активна'):
            expect(button).to_be_visible()
            expect(button).to_be_enabled()

    @allure.story("Name length validation")
    @allure.title("Перевірка довжини імені")
    def test_length_name_symbols_field(self, pw_page, registering_page):
        with allure.step('Ввести занадто коротке/довге ім\'я'):
            registering_page.length_name_symbols_field()
        with allure.step('Перевірити повідомлення про помилку'):
            expect(registering_page.page.locator(
                registering_page.page_locators.length_name_not_valid_message)).to_be_visible()

    @allure.story("Digits in name validation")
    @allure.title("Перевірка цифр у полі імені")
    def test_digits_in_name_symbols_field(self, pw_page, registering_page, trace_per_test):
        with allure.step('Ввести ім\'я з цифрами'):
            registering_page.digits_in_name_symbols_field()
        with allure.step('Перевірити повідомлення про помилку'):
            expect(registering_page.page.locator(
                registering_page.page_locators.symbols_name_not_valid_message)).to_be_visible()

    @allure.story("Passwords identical validation")
    @allure.title("Перевірка збігу паролів")
    def test_is_passwords_identical(self, pw_page, registering_page):
        with allure.step('Ввести два різні паролі'):
            registering_page.is_passwords_identical()
        with allure.step('Перевірити повідомлення про невідповідність паролів'):
            expect(registering_page.page.locator(
                registering_page.page_locators.password_identically_message)).to_be_visible()
