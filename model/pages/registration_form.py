from selene.support.shared.jquery_style import s
from selene import have
from selene import command
from selene.support.shared import browser
from model.controls import dropdown, modal, datepicker
from model.controls.checkbox import select_checkbox
from model.data.user import Hobby, Subject



class RegistrationForm:
    def open_page(self, url, resourses):
        br = browser.open(url + resourses)
        browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').with_(timeout=15) \
            .should(have.size_less_than_or_equal(10)) \
            .perform(command.js.remove)
        return self

    def take_first_name(self, name: str):
        browser.element('#firstName').type(name)
        return self

    def take_last_name(self, last_name: str):
        browser.element('#lastName').type(last_name)
        return self

    def take_email(self, email: str):
        browser.element('#userEmail').type(email)
        return self

    def take_phone_number(self, number: str):
        browser.element('#userNumber').type(number)
        return self


    def choose_birthday(self, birth_day, birth_month, birth_year):
        birtday = datepicker.DatePicker()
        birtday.choose_date(birth_day, birth_month, birth_year, '#dateOfBirthInput')
        return self

    def take_hobby(self, hobbies: Hobby):
        for hobby in hobbies:
            select_checkbox('[for^=hobbies-checkbox]', hobby.name).first.click().perform(command.js.scroll_into_view)
        return self
    def take_subject(self,subjects: Subject):
        for subject in subjects:
            browser.element('[id="subjectsInput"]').type(subject.name).press_enter()
        return self

    def take_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def scroll_to_bottom(self):
        s('#state').perform(command.js.scroll_into_view)

    def take_state(self, value: str):
        st = dropdown.DropDown()
        st.select(browser.element('#state'), value)
        return self

    def take_city(self, value: str):
        sity = dropdown.DropDown()
        sity.select(browser.element('#city'), value)
        return self


   # def take_picture(relative_path) -> str:
        #path = str(Path(__file__).parent.parent.joinpath('resources').joinpath(relative_path))
       # return path

    def set_gender(self, gender):
        browser.all('[for^=gender-radio]').all_by(
            have.exact_text(gender)
        ).first.click()
        return self



    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self

        # def should_have_submitted(data):
        #  rows = modal.dialog.all('tbody tr')
        #  for row, value in data:
        # rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))

    def should_have_submitted(self, data):
        dialog = browser.element('.modal-content')
        rows = dialog.all('tbody tr')
        for row, value in data:
            rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
            return self

