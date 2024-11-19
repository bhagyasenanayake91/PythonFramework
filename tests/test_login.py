from playwright.sync_api import expect

from pages.LoginPage import Login

user = {
    "username": "standard_user",
    "password": "secret_sauce"
}

class TestLogin:
    def test_login(self, page):
        login_page = Login(page)
        login_page.navigate()
        login_page.submit_login(user)
        expect(page.locator('//*[@id="header_container"]/div[2]/span')).to_contain_text('Products')

