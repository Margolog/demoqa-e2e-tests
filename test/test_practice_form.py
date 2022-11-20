from model.apps import app
from model.data.user import Margo


# FluentPageObjects

def test_submit_student_registration_form():
    (app.registration_form.open_page('https://demoqa.com', '/automation-practice-form')

        .take_first_name(Margo.name)
        .take_last_name(Margo.last_name)
        .take_email(Margo.email)
        .set_gender(Margo.gender.value)
        .take_phone_number(Margo.number)
        .choose_birthday(Margo.birth_day, Margo.birth_month, Margo.birth_year)
        .take_hobby(Margo.hobbies)
        .take_subject(Margo.subject)
        #.take_photo(Margo)
        .take_address(Margo.address)
        .take_state(Margo.state)
        .take_city(Margo.city)
        .submit()

        .should_have_submitted(
        [
            ('Student Name', f'{Margo.name} {Margo.last_name}'),
            ('Student Email', Margo.email),
            ('Gender', Margo.gender),
            ('Mobile', Margo.number),
            ('Subjects', Margo.subject),
            ('Hobbies', Margo.hobbies),
            ('Picture', Margo.photo),
            ('Address', Margo.address),
            ('State and City', f'{Margo.state} {Margo.city}'),
        ],
    )
    )


# StepsObject
def test_register_user():
    app.register_user.registration()