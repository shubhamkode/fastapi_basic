import sqlalchemy.orm as _orm

import src.config.config as _database
import src.models.models as _models
import src.schemas.schemas as _schemas

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_users(db: _orm.Session):
    return db.query(_models.User).all()

def add_users(user: _schemas.UserCreate, db: _orm.Session):
    user_obj = _models.User(**user.dict())
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


