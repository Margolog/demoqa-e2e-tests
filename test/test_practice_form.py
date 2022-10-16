from model.pages import registration_form
from model.utils import *


def test_submit_student_registration_form():
    # GIVEN
    registration_form.open_page('https://demoqa.com', '/automation-practice-form')

    # WHEN
    registration_form.take_first_name('Margo')
    registration_form.take_last_name('Log')
    registration_form.take_email('Logunovar@gmail.com')
    registration_form.choose_gender()
    registration_form.take_phone_number('9876543211')
    registration_form.choose_birthday()
    registration_form.take_hobbies()
    registration_form.take_subject('Hindi')
    registration_form.take_picture('../resourses/pic.jpg')
    registration_form.take_address('Saint-Peterburg')
    registration_form.take_state('Haryana')
    registration_form.take_city('Karnal')
    registration_form.submit()
    # ASSERT
    registration_form.should_have_submitted(
        [
            ('Student Name', 'Margo Log'),
            ('Student Email', 'Logunovar@gmail.com'),
            ('Gender', 'Female'),
            ('Mobile', '9876543211'),
            ('Date of Birth', '12 March,1996'),
            ('Subjects', 'Computer Science'),
            ('Hobbies', 'Sports'),
            ('Picture', 'pic.jpg'),
            ('Address', 'Saint-Peterburg'),
            ('State and City', 'Haryana Karnal')
        ]
    )
