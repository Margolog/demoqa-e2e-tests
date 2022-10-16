import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 5
    browser.config.base_url = ('https://demoqa.com/automation-practice-form')
    browser.config.browser_name = 'chrome'


    yield
