import os.path
import allure
from model.apps import app
from model.pages import registration_form


def take_first_name(param):
    pass


def test_submit_student_registration_form():
    app.registration_form.open_page('https://demoqa.com', '/automation-practice-form')

    (app.registration_form
        .take_first_name('Margo').take_last_name('Log')
        .take_email('Logunovar@gmail.com')
        .choose_gender()
        .take_phone_number('9876543211')
        #.scroll_to_bottom()
        .choose_birthday()
        .take_hobbies()
        .take_subject('Hindi')
        .take_picture('../resources/pic.jpg')
        #.take_picture(take_picture('pic.jpg'))
        #.take_address('Saint-Peterburg')
        #.scroll_to_state()
        .take_state('Haryana')
        .take_city('Karnal')
        .submit()

        .should_have_submitted(
            ('Student Name', 'Margo Log'),
            ('Student Email', 'Logunovar@gmail.com'),
            ('Gender', 'Female'),
            ('Mobile', '9876543211'),
            ('Date of Birth', '12 March,1996'),
            ('Subjects', 'Hindi'),
            ('Hobbies', 'Sports'),
            ('Picture', 'pic.jpg'),
            ('Address', 'Saint-Peterburg'),
            ('State and City', 'Haryana Karnal')
    )
)
