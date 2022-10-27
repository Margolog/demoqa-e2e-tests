import os

import pytest
from selene import be, have
from selene import command
from selene.support.shared import browser
from model.controls import dropdown, modal, datepicker
from selene.support.shared.jquery_style import s
from pathlib import Path


def open_page(url, resourses):
#    br = browser.open(url + resourses)
    #    if br.with_(timeout=6).wait.until(have.size_greater_than_or_equal(3)):
    #        br.perform(command.js.remove)
    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').with_(timeout=10) \
        .should(have.size_less_than_or_equal(4)) \
        .perform(command.js.remove)


def take_first_name(firstname):
    browser.element('#firstName').type(firstname)


def take_last_name(lastname):
    browser.element('#lastName').type(lastname)


def take_email(email):
    browser.element('#userEmail').type(email)


def take_phone_number(mobile):
    browser.element('#userNumber').type(mobile)


def choose_birthday():
    datepicker.fill_2_date()


# def fill_birthday(date: datetime.date):
#    datepicker.select_date(birthday, date)


def take_subject(subject):
    browser.element('#subjectsInput').should(be.blank).type(subject).press_enter()


def take_hobbies():
    browser.element('#hobbies-checkbox-1').perform(command.js.click)


def take_address(address):
    browser.element('#currentAddress').type(address)


def scroll_to_bottom():
    s('#state').perform(command.js.scroll_into_view)


def take_state(value: str):
    dropdown.select(browser.element('#state'), value)


def take_city(value: str):
    dropdown.select(browser.element('#city'), value)


def abs_path(relative_path):
    path = os.path.abspath(relative_path)
    return path


# def take_picture(photo):
#    browser.element('[id="uploadPicture"]').send_keys(abs_path(photo))


def take_picture(relative_path) -> str:
    path = str(Path(__file__).parent.parent.joinpath('resources').joinpath(relative_path))
    return path


def choose_gender():
    browser.element("[for='gender-radio-2']").perform(command.js.click)


def submit():
    browser.element('#submit').perform(command.js.click)


def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
