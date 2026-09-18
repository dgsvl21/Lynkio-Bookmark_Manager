from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.api.dependencies import get_current_user
from app.models.user import User
from app.schemas.bookmark import BookmarkCreate, BookmarkResponse, BookmarkUpdate
from app.services.bookmark_service import create_bookmark, delete_bookmark, get_bookmark_by_id, update_bookmark
from app.services.bookmark_service import get_user_bookmarks, create_bookmark
from uuid import UUID
from fastapi import HTTPException

router = APIRouter(
    prefix="/bookmarks",
    tags=["bookmarks"]
)

@router.post("", response_model=BookmarkResponse)
def create_bookmark_endpoint(bookmark: BookmarkCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_bookmark(db, current_user.id, bookmark)

@router.get("", response_model=list[BookmarkResponse])
def get_bookmarks(db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_user_bookmarks(db, current_user.id)

@router.get("/{bookmark_id}", response_model=BookmarkResponse)
def get_bookmark(bookmark_id:UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    bookmark = get_bookmark_by_id(db, bookmark_id, current_user.id)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return bookmark

@router.put("/{bookmark_id}", response_model=BookmarkResponse)
def update_existing_bookmark(bookmark_id: UUID, bookmark_data: BookmarkUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    bookmark = get_bookmark_by_id(db, bookmark_id, current_user.id)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return update_bookmark(db, bookmark, bookmark_data)

@router.delete("/{bookmark_id}")
def delete_existing_bookmark(
    bookmark_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    bookmark = get_bookmark_by_id(db, bookmark_id, current_user.id)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    delete_bookmark(db, bookmark)
    return {"message": "Bookmark deleted successfully"}