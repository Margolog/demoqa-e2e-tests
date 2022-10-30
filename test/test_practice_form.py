import os.path

import allure
from model.pages import registration_form
from model.pages.registration_form import take_picture



def test_submit_student_registration_form():
    # GIVEN
    with allure.step("Открываем страницу регистрации"):
        registration_form.open_page('https://demoqa.com', '/automation-practice-form')

    # WHEN
    with allure.step("Заполняем форму для регистрации"):
        registration_form.take_first_name('Margo')
        registration_form.take_last_name('Log')
        registration_form.take_email('Logunovar@gmail.com')
        registration_form.choose_gender()
        registration_form.take_phone_number('9876543211')
        registration_form.scroll_to_bottom()
        registration_form.choose_birthday()
        registration_form.take_hobbies()
        registration_form.take_subject('Hindi')
        # registration_form.take_picture('../resources/pic.jpg')
        registration_form.take_picture(take_picture('pic.jpg'))
        registration_form.take_address('Saint-Peterburg')
        registration_form.scroll_to_bottom()
        registration_form.take_state('Haryana')
        registration_form.take_city('Karnal')
        registration_form.submit()

    # ASSERT
    with allure.step("Проверяем заполненную форму"):
        registration_form.should_have_submitted(
            [
                ('Student Name', 'Margo Log'),
                ('Student Email', 'Logunovar@gmail.com'),
                ('Gender', 'Female'),
                ('Mobile', '9876543211'),
                ('Date of Birth', '12 March,1996'),
                ('Subjects', 'Hindi'),
                ('Hobbies', 'Sports'),
#                ('Picture', 'pic.jpg'),
                ('Address', 'Saint-Peterburg'),
                ('State and City', 'Haryana Karnal')
            ]
        )
