from playwright.sync_api import Page

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_btn = page.locator("button[type='submit']")
        self.success_msg = page.locator(".flash.success")
        self.error_msg = page.locator(".flash.error")
        self.logout_btn = page.locator("a[href='/logout']")

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_btn.click()

    def is_success_visible(self):
        return self.success_msg.is_visible()

    def is_error_visible(self):
        return self.error_msg.is_visible()

    def get_error_text(self):
        return self.error_msg.inner_text()
