from models import *
from pprint import pprint
from sqlalchemy import func,desc

x = session.query(Students.name, func.round(func.avg(Grades.grade))).label("average_grade")\
    .select_from()