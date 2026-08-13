from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password
from app.core.security import verify_password

def get_user_by_email(
    db: Session,
    email: str
):
    return(
        db.query(User)
        .filter(User.email == email)
        .first()
    )

def create_user(
        db: Session,
        user_data: UserCreate
):
    user = User(
        email=user_data.email.lower(),
        username=user_data.username,
        password_hash=hash_password(user_data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

def authenticate_user(
        db,
        username: str,
        password: str
):
    user= get_user_by_email(db, username)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user