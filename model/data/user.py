from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    Hindi = 'Hindi'


class Hobby(Enum):
    Sports = '1'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    gender: Gender
    name: str
    last_name: str = 'Log'
    email: str = 'Logunovar@gmail.com'
    number: str = '891111111111'
    birth_day: str = '12'
    birth_month: str = 'March'
    birth_year: str = '1996'
    subject = Subject.Hindi,
    hobbies = Hobby.Sports,
    address: str = 'Saint-Peterburg'
    photo: str = 'pic.jpg'
    state: str = 'Haryana'
    city: str = 'Karnal'


Margo = User(name='Margo', gender=Gender.Female)