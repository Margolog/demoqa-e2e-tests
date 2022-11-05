import os

import pytest
import self as self
from selene import be, have
from selene import command
from selene.support.shared import browser
from model.controls import dropdown, modal, datepicker
from selene.support.shared.jquery_style import s
from pathlib import Path

from model.controls.datepicker import DatePicker
from model.controls.dropdown import DropDown



class RegistrationForm:
    def open_page(self, url, resourses):
        br = browser.open(url + resourses)
        browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').with_(timeout=15) \
            .should(have.size_less_than_or_equal(10)) \
            .perform(command.js.remove)
        return self

    def take_first_name(self, firstname: str):
        browser.element('#firstName').type(firstname)
        return self

    def take_last_name(self, lastname: str):
        browser.element('#lastName').type(lastname)
        return self

    def take_email(self, email: str):
        browser.element('#userEmail').type(email)
        return self

    def take_phone_number(self, mobile: str):
        browser.element('#userNumber').type(mobile)
        return self

    def choose_birthday(self):
        birthday_datepicker = DatePicker()
        birthday_datepicker.fill_2_date()
        return self


    def take_subject(self, subject):
        browser.element('#subjectsInput').should(be.blank).type(subject).press_enter()
        return self

    def take_hobbies(self):
        browser.element('#hobbies-checkbox-1').perform(command.js.click)
        return self

    def take_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def take_state(self, value):
        self.s('#state').perform(command.js.scroll_into_view)
        DropDown.select(self, browser.element('#state'), value)
        return self

    def take_city(self, value):
        DropDown.select(self, browser.element('#city'), value)
        return self

    def abs_path(self, relative_path):
        path = os.path.abspath(relative_path)
        return path
        return self

#   def take_picture(self, photo):
 #       browser.element('[id="uploadPicture"]').send_keys(photo.abs_path(photo))
  #      return self

    def take_picture(self, relative_path) -> str:
        path = str(Path(__file__).parent.parent.joinpath('resources').joinpath(relative_path))
        return path
        return self

    def choose_gender(self):
        browser.element("[for='gender-radio-2']").perform(command.js.click)
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
