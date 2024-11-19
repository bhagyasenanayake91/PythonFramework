from playwright.sync_api import sync_playwright, expect

from pages.HomePage import Login


user = {
    "username": "btest1",
    "password": "Test123"
}

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     login_page = Login(page)
#     login_page.navigate()
#     login_page.submit_login(user)
#     expect(page.locator('//*[@id="showOverview"]/h1')).to_contain_text('Accounts Overview')

#     browser.close()
class TestLogin:
    def test_login(self, page):
        
        # browser = pagechromium.launch(headless=False)
        # page = browser.new_page()
        login_page = Login(page)
        login_page.navigate()
        login_page.submit_login(user)
        expect(page.locator('//*[@id="showOverview"]/h1')).to_contain_text('Accounts Overview')

        # browser.close()


