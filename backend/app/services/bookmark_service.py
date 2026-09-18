from requests import session
from sqlalchemy.orm import Session
from app.models.bookmark import Bookmark
from app.schemas.bookmark import BookmarkCreate

def create_bookmark(db: Session, user_id: int, bookmark_data: BookmarkCreate):
    bookmark = Bookmark(
        user_id=user_id,
        url=bookmark_data.url,
        title=bookmark_data.title,
        description=bookmark_data.description
    )
    db.add(bookmark)
    db.commit()
    db.refresh(bookmark)
    
    return bookmark

def get_user_bookmarks(
    db: Session,
    user_id
):
    return (
        db.query(Bookmark)
        .filter(Bookmark.user_id == user_id)
        .all()
    )

def get_bookmark_by_id(
        db: Session,
        bookmark_id,
        user_id
):
    return (
        db.query(Bookmark)
        .filter(Bookmark.id == bookmark_id, Bookmark.user_id == user_id)
        .first()
    )

def update_bookmark(
        db: Session,
        bookmark,
        bookmark_data,
):
    update_data = bookmark_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(bookmark, field, value)
    db.commit()
    db.refresh(bookmark)

    return bookmark

def delete_bookmark(
        db: Session, 
        bookmark
):
    db.delete(bookmark)
    db.commit()