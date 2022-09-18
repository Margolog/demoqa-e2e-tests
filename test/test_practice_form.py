from selene.support.shared import browser
from selene import have, be, command
from selene.support import by
import os
from selene.support.shared.jquery_style import s, ss

def test_tools_qa(browser_management):
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element('#firstName').type('Margo')
    browser.element('#lastName').type('Log')
    browser.element('#userEmail').type('Logunovar@gmail.com')
    browser.element('[id^=gender-radio][value=Female]').perform(command.js.click)
    browser.element('#userNumber').type('9876543211')
    browser.element('#dateOfBirthInput').double_click()
    browser.element('.react-datepicker__year-select').type('1996')
    browser.element('.react-datepicker__month-select').type('March')
    browser.element('.react-datepicker__day--012').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('#hobbies-checkbox-1').perform(command.js.click)
    browser.element('#uploadPicture').send_keys(os.path.abspath('../resourses/pic.jpg'))
    browser.element('#currentAddress').type('Saint-Peterburg')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Gurgaon').press_enter()
    browser.element('#submit').press_enter()

#ASSERT
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.modal-body td+td').should(have.texts(
        'Margo Log',
        'Logunovar@gmail.com',
        'Female',
        '9876543211',
        '12 March,1996',
        'Computer Science',
        'Sports',
        'pic.jpg',
        'Saint-Peterburg',
        'NCR Gurgaon'))