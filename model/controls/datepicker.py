
from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys


class DatePicker:
    def choose_date(self, day, month, year, selector):
        browser.element(selector).click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(
            f'.react-datepicker__day--0{day}'
            f':not(.react-datepicker__day--outside-month)'
        ).click()

    def choose_date_by_typing(self, selector):
            browser.element(selector).send_keys(Keys.CONTROL, 'a').type('12 Mar 1996').press_enter()