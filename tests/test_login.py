def test_page_opens(login_page):
    assert "login" in login_page.page.url

def test_successful_login(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert login_page.is_success_visible()

def test_logout_after_login(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    login_page.logout_btn.click()
    assert "login" in login_page.page.url

def test_wrong_password(login_page):
    login_page.login("tomsmith", "wrongpassword")
    assert login_page.is_error_visible()

def test_wrong_username(login_page):
    login_page.login("wronguser", "SuperSecretPassword!")
    assert login_page.is_error_visible()

def test_empty_credentials(login_page):
    login_page.login("", "")
    assert login_page.is_error_visible()

def test_error_message_content(login_page):
    login_page.login("wronguser", "wrongpass")
    error_text = login_page.get_error_text()
    assert "Your username is invalid" in error_text
