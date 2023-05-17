from datetime import date, datetime, timedelta
from pprint import pprint
from random import choice, randint

import faker

from models import *

fake = faker.Faker()

STUDENTS = 50
TEACHERS = 5
GROUPS = ["СБУ-14","ПГС-13","АРХ-12"]
SUBJECTS = [
    "English Language",
    "Mathematic",
    "History",
    "Programming",
    "Biology",
    "Physics",
    "Chemistry",
    "Astronomy",
    "Ukrainian Language",
    "Design",
    "Spain Language",
    "Geography",
    "Geometry",
    "French Language"
    ]


def seed_students():
    adding = []
    for i in range(1,STUDENTS+1):
        adding.append((Students(name = fake.name(), group_id = randint(1,len(GROUPS)))))
    session.add_all(adding)
    session.commit()



