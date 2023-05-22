from playwright.sync_api import sync_playwright, Page
import pytest

def test_title(page: Page):
    sauceURL = 'https://www.saucedemo.com/'
    page.goto(sauceURL)
    assert page.title() == 'Swag Labs'