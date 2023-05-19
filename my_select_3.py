from models import *
from pprint import pprint
from sqlalchemy import func,desc

x = session.query(Groups.name, Subjects.name, func.round(func.avg(Grades.grade)).label("average_grade"))\
.select_from(Grades).join(Students).join(Subjects).join(Groups)\
.group_by(Groups.name).order_by(desc("average_grade")).where(Subjects.id  ==5).all()
                  
                  

pprint(x)