import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from selene.support.shared import browser
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse='true')
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 5
    browser.config.base_url = ('https://demoqa.com/automation-practice-form')
    browser.config.browser_name = 'chrome'
    browser.config.window_width, browser.config.window_height = 1920, 1024

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('login')
    password = os.getenv('password')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    #    driver = webdriver.Remote(
    #        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
    #        options=options)

    browser.config.driver = driver

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
