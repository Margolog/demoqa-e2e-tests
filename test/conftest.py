import pytest
from selene.support.shared import browser
from selene import be, have
from selene import command


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 5
    browser.config.base_url = ('https://demoqa.com/automation-practice-form')
    browser.config.browser_name = 'chrome'
    browser.config.window_width, browser.config.window_height = 1920, 1024


