from sqlalchemy import create_engine, select, and_, or_, func, update, delete
from sqlalchemy.orm import sessionmaker

from assoc_table import student_course
from students_table import Student
from courses_table import Course
from base_tables import Base

from faker import Faker

local_faker = Faker()

engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

session.execute(delete(student_course))
session.execute(delete(Student))
session.execute(delete(Course))
session.commit()

python = Course(name="Python")
php = Course(name="PHP")
aqa = Course(name="AQA")
c_plus = Course(name="C++")
c_sharp = Course(name="C#")

alice = Student(name="Alice")
bob = Student(name="Bob")
natali = Student(name="Natali")
ivano = Student(name="Ivano")
kate = Student(name="Kate")
michelson = Student(name="Michelson")
dikson = Student(name="Dikson")
alex = Student(name="Alex")
sam = Student(name="Samantha")
nick = Student(name="Nick")

alice.courses.extend([python, php])
bob.courses.append(c_plus)
natali.courses.extend([c_plus, php])
ivano.courses.extend([c_sharp, php])
kate.courses.extend([c_plus, python])
michelson.courses.extend([php, c_sharp, c_plus])
dikson.courses.append(python)
alex.courses.extend([python, php, c_plus, c_sharp])
sam.courses.extend([php, c_plus])
nick.courses.extend([python, c_sharp])

session.add_all([
    python, php, aqa, c_plus, c_sharp,
    alice, bob, natali, ivano, kate,
    michelson, dikson, alex, sam, nick
])
session.commit()

# adding a new student
new_student = Student(name="Tylor")
session.add(new_student)

python_course = session.query(Course).filter_by(name="Python").first()
c_plus_course = session.query(Course).filter_by(name="C++").first()

new_student.courses.extend([python_course, c_plus_course])

session.commit()


for course in session.query(Course).all():
    print('Course', course.name, "is visited by", [s.name for s in course.students])
print('_'*80)

for student in session.query(Student).all():
    print(student.name, "added to", len(student.courses), 'courses:',
          [course.name for course in student.courses])
print('_'*80)

first_student = session.query(Student).first()

print(first_student.name, "added to", len(first_student.courses), 'courses:',
      [course.name for course in first_student.courses])
print('_'*80)