from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.conn import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)

    courses = relationship("Course", back_populates="user")
    registries = relationship("Registry", back_populates="user")
    reviews = relationship("Review", back_populates="user")


class CategoryCourse(Base):
    __tablename__ = "category_course"

    course_id = Column(Integer, ForeignKey("course.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("category_name.id"), primary_key=True)


class Category(Base):
    __tablename__ = "category_name"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)

    courses = relationship(
        "Course", secondary=CategoryCourse.__table__, back_populates="categories"
    )


class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    course_load = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="courses")
    lessons = relationship("Lesson", back_populates="course")
    registries = relationship("Registry", back_populates="course")
    reviews = relationship("Review", back_populates="course")

    categories = relationship(
        "Category", secondary=CategoryCourse.__table__, back_populates="courses"
    )


class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    video_uuid = Column(String, nullable=False)
    course_id = Column(Integer, ForeignKey("course.id"))

    course = relationship("Course", back_populates="lessons")


class Registry(Base):
    __tablename__ = "registry"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    is_teacher = Column(Boolean, nullable=False)
    course_id = Column(Integer, ForeignKey("course.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="registries")
    course = relationship("Course", back_populates="registries")


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    grade = Column(Integer, nullable=False)
    course_id = Column(Integer, ForeignKey("course.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="reviews")
    course = relationship("Course", back_populates="reviews")
