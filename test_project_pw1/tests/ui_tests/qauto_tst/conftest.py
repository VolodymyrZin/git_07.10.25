import pytest

from definitions import BASE_PATH
from playwright.sync_api import sync_playwright, expect

from test_project_pw1.core.ui.qauto.pages.main_page.main_page import MainPage


@pytest.fixture(scope="function", autouse=True)
def trace_per_test(request, pw_page):

    context = pw_page.context

    trace_path = BASE_PATH / 'pw_traces_new'
    trace_path.mkdir(exist_ok=True)

    # старт трасування
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield  # тест виконується тут

    # stop tracing і збереження після тесту
    test_name = request.node.name
    context.tracing.stop(path=str(trace_path / f"{test_name}.zip"))


@pytest.fixture
def pw_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(
            http_credentials={
                "username": "guest",
                "password": "welcome2qauto"
            }
        )
        yield page
        browser.close()

@pytest.fixture
def registering_page(pw_page):
    main_page = MainPage(pw_page)
    main_page.open_page()

    login_page = main_page.click_sign_in()
    registering_page = login_page.click_registration_button()
    yield registering_page

@pytest.fixture
def main_page(pw_page):
    main_page = MainPage(pw_page)
    main_page.open_page()
    yield main_page

