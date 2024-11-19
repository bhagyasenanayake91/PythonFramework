from playwright.sync_api import expect

from pages.HomePage import Login

user = {
    "username": "btest1",
    "password": "Test123"
}

class TestLogin:
    def test_login(self, page):
        login_page = Login(page)
        login_page.navigate()
        login_page.submit_login(user)
        expect(page.locator('//*[@id="showOverview"]/h1')).to_contain_text('Accounts Overview')

