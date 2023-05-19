from models import *
from pprint import pprint
from sqlalchemy import func,desc
x = session.query(Students.name, func.round(func.avg(Grades.grade),2).label("avg_grade"))\
.select_from(Grades).join(Students).group_by(Students.id).order_by(desc("avg_grade")).limit(5).all()


pprint(x)

# example = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
#         .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()