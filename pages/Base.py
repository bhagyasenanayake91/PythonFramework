from playwright.sync_api import Page


class Base:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://parabank.parasoft.com/parabank/index.htm"