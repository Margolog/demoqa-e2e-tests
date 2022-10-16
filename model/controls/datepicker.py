
from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys


def input(day: str, month: str, year: str):
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL+'a').type(day+month+year).press_enter()


def fill_2_date():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').type('1996')
    browser.element('.react-datepicker__month-select').type('March')
    browser.element('.react-datepicker__day--012').click()