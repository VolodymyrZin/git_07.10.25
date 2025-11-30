from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from base_tables import Base
from assoc_table import student_course


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)

    courses = relationship(
        "Course",
        secondary=student_course,
        back_populates="students", )
