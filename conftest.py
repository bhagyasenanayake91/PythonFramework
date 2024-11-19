# import pytest
# from playwright.sync_api import sync_playwright
# from requests import request

# def pytest_addoption(parser):
#     parser.addoption("--headed", action="store_true", default=True, help="Run browser in headed mode")


#     @pytest.fixture(scope="session")
#     def playwright():
#         with sync_playwright() as playwright_instance:
#             yield playwright_instance
    
    
#     @pytest.fixture(scope="session")
#     def browser(playwright):
#         headless_mode = request.config.getoption("--headed")
#         browser = playwright.firefox.launch(headless=headless_mode)  # Set headless=True for headless mode
#         yield browser
#         browser.close()
    
#     @pytest.fixture(scope="function")
#     def browser_context(browser):
#         context = browser.new_context()
#         yield context
#         context.close()
    
    
#     @pytest.fixture(scope="function")
#     def set_up_tear_down(browser_context):
#         page = browser_context.new_page()
#         page.set_viewport_size({"width": 1536, "height": 800})
#         page.goto("https://www.saucedemo.com/")
#         yield page
#         page.close()
    