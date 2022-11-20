from selene import have, command
from selene.support.shared import browser


class DropDown:
    def select(self, element, option):
        element.click()
        browser.all('[id^=react-select][id*=-option-]').find_by(have.exact_text(option)).click()
        return self