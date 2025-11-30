from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from base_tables import Base
from assoc_table import student_course


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)


    students = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses")