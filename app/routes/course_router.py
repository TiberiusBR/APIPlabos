from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repository import course_repo as repo
from repository import category_course_repo
from schemas import course as course_schema
from schemas import category_course as cat_course_schema
from schemas.category_course import CategoryCourseCreate
from database.conn import get_db

course_router = APIRouter(prefix="/course")


@course_router.get("/", response_model=list[course_schema.CourseAuthorCategory])
def get_courses(db: Session = Depends(get_db)):
    courses = repo.get_all_courses(db)
    return courses


@course_router.get("/id/{course_id}", response_model=course_schema.CourseAuthorCategory)
def get_course_by_id(course_id: int, db: Session = Depends(get_db)):
    course = repo.get_course_by_id(db, course_id)
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="No course found."
        )
    return course


@course_router.get("/author/name/{name}", response_model=list[course_schema.CourseAuthorCategory])
def get_courses_by_author_name(name: str, db: Session = Depends(get_db)):
    courses = repo.get_courses_by_author_name(db, name)
    if not courses:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="No course found."
        )
    return courses


@course_router.get("/author/id/{author_id}", response_model=list[course_schema.CourseAuthorCategory])
def get_courses_by_author_id(author_id: int, db: Session = Depends(get_db)):
    courses = repo.get_courses_by_author_id(db, author_id)
    if courses is None:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="No course found."
        )
    return courses


@course_router.get("/title/{name}", response_model=list[course_schema.CourseAuthorCategory])
def get_courses_by_title(name: str, db: Session = Depends(get_db)):
    courses = repo.get_courses_by_title(db, name)
    if courses is None:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="No course found."
        )
    return courses


@course_router.get("/category/{category_id}", response_model=list[course_schema.CourseAuthorCategory])
def get_courses_by_category(category_id: int, db: Session = Depends(get_db)):
    courses = repo.get_course_by_category(db, category_id)
    if courses is None:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="No courses found."
        )
    return courses


@course_router.post("/create", response_model=course_schema.Course)
def create_course(course: course_schema.CourseBase, db: Session = Depends(get_db)):
    created_course = repo.create_course(db, course)
    return created_course


@course_router.post(
    "/category", response_model=list[cat_course_schema.CategoryCourseCreate]
)
def insert_categories(
    cat_course_payload: cat_course_schema.CategoryCoursePayload,
    db: Session = Depends(get_db),
):
    if len(cat_course_payload.category_ids) < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Must insert at least one category id.",
        )
    course_id = cat_course_payload.course_id
    categories_id = cat_course_payload.category_ids
    new_cats_course = [
        CategoryCourseCreate(course_id=course_id, category_id=cat_id)
        for cat_id in categories_id
    ]
    new_cats_course = category_course_repo.create_category_course(new_cats_course, db)
    return new_cats_course


@course_router.get("/learning/{user_id}", response_model=list[course_schema.Course])
def get_course_by_id(user_id: int, db: Session = Depends(get_db)):
    courses = repo.get_courses_learning_by_user_id(db, user_id)
    if len(courses) == 0:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="No course found."
        )
    return courses