from playwright.sync_api._generated import ElementHandle

from pages.Base import Base

class Login(Base):
    def __init__(self, page):
        self.page = page
        self.base_url = "https://parabank.parasoft.com/parabank/index.htm"

    @property
    def  username_field(self):
            return self.page.locator("input[name=\"username\"]")
    
    @property
    def  password_field(self):
            return self.page.locator("input[name=\"password\"]")
    
    @property
    def  login_button(self):
            return self.page.get_by_role("button", name="Log In")

    def submit_login(self, user):
          self.username_field.fill(user["username"])
          self.password_field.fill(user["password"])
          self.login_button.click()

    def navigate(self):
          self.page.goto(f"{self.base_url}")