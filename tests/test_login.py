import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_valid_login(page):
    login_page=LoginPage(page)
    login_page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user","secret_sauce")
    page.wait_for_url("**/inventory.html")
    assert page.locator("//div[@class='app_logo']").is_visible()