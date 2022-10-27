from selene import have
from selene.support.shared import browser


def select(element, option):
    element.click()
    browser.all('[id^=react-select][id*=-option-]').find_by(have.exact_text(option))  # .click()
    browser.element("#city").click()
