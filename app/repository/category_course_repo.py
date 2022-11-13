from sqlalchemy.orm import Session
from app.models import models
from app.schemas.category_course import CategoryCourseCreate


def create_category_course(cats_course_list: list[CategoryCourseCreate], db: Session):
    new_cats_course = [
        models.CategoryCourse(**cat_course.dict()) for cat_course in cats_course_list
    ]
    db.add_all(new_cats_course)
    db.commit()
    [db.refresh(new_cat) for new_cat in new_cats_course]
    return new_cats_course
