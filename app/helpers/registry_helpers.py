from repository import user_repo
from repository import course_repo
from repository import registry_repo
from sqlalchemy.orm import Session


def is_existing_course(db: Session, course_id: int) -> bool:
    course = course_repo.get_course_by_id(db, course_id)
    if course:
        return True
    return False


def is_existing_user(db: Session, user_id: int) -> bool:
    user = user_repo.get_user_by_id(db, user_id)
    if user:
        return True
    return False


def is_registration_user(db: Session, user_id: int, course_id: int) -> bool:
    record = registry_repo.get_registration_by_user_and_course(db, user_id, course_id)
    if record:
        return True
    return False
