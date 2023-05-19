from models import *
from pprint import pprint
from sqlalchemy import func,desc

x = session.query(Students.name, func.round(func.avg(Grades.grade),2).label("average_grade"))\
    .select_from(Grades).join(Students).join(Subjects)\
    .group_by(Students.id).order_by(desc("average_grade")).where(Subjects.id == 5)\
    .first()

pprint(x)