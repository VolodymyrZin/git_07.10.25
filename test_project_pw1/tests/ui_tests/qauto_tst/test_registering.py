import pytest

from test_project_pw1.core.ui.qauto.pages.login_page.login_page import LoginPage
from test_project_pw1.utils.settings import d_settings
from test_project_pw1.core.ui.qauto.pages.main_page.main_page import MainPage
from playwright.sync_api import sync_playwright, expect
from definitions import BASE_PATH
import time
import pathlib

# шлях до кореня проєкту
# BASE_PATH = pathlib.Path(__file__).parent


def test_smoke_main_page(pw_page, main_page):
    assert main_page.is_page_opened() is True, 'Home page was\'nt opened'
    pw_page.wait_for_timeout(1000)

def test_login_modal(pw_page, main_page):
    login_page = main_page.click_sign_in()
    assert login_page.is_page_opened(), "Login modal wasn't opened"
    pw_page.wait_for_timeout(1000)

def test_register_modal(pw_page, main_page):
    login_page = main_page.click_sign_in()
    assert login_page.is_page_opened(), "Login modal wasn't opened"
    pw_page.wait_for_timeout(1000)

    registering_page = login_page.click_registration_button()
    assert registering_page.is_page_opened(), "Registration modal wasn't opened"
    pw_page.wait_for_timeout(1000)

def test_is_fields_visible(pw_page, main_page):
    login_page = main_page.click_sign_in()
    registering_page = login_page.click_registration_button()
    assert registering_page.is_fields_visible(), 'Fields are not visible'
    pw_page.wait_for_timeout(1000)

def test_required_fields(pw_page, registering_page):
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
            fields[i+1].click()
        else:
            registering_page.page.locator("body").click()
        expect(error).to_be_visible()
    pw_page.wait_for_timeout(1000)

def test_register_button_enabled(pw_page, registering_page):
    button = registering_page.page.locator(registering_page.page_locators.registering_button)
    expect(button).to_be_disabled()

    registering_page.page.fill(registering_page.page_locators.user_name, "Test")
    registering_page.page.fill(registering_page.page_locators.last_name, "User")
    registering_page.page.fill(registering_page.page_locators.email, "testuser@example.com")
    registering_page.page.fill(registering_page.page_locators.user_pwd, "Password123!")
    registering_page.page.fill(registering_page.page_locators.user_reenter_pwd, "Password123!")

    expect(button).to_be_visible()
    expect(button).to_be_enabled()



def test_length_name_symbols_field(pw_page, registering_page):
    registering_page.length_name_symbols_field()
    expect(registering_page.page.locator(registering_page.page_locators.length_name_not_valid_message)).to_be_visible()

def test_digits_in_name_symbols_field(pw_page, registering_page, trace_per_test):
    registering_page.digits_in_name_symbols_field()
    expect(registering_page.page.locator(registering_page.page_locators.symbols_name_not_valid_message)).to_be_visible()


def test_is_passwords_identical(pw_page, registering_page):
    registering_page.is_passwords_identical()
    expect(registering_page.page.locator(registering_page.page_locators.password_identically_message)).to_be_visible()
