import fastapi as _fastapi
import typing as _typing
import sqlalchemy.orm as _orm

import src.services.services as _services
import src.schemas.schemas as _schemas

router = _fastapi.APIRouter(prefix="/users")

_services.create_database()

@router.get("/", response_model=_typing.List[_schemas.User])
def get_users(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    users =  _services.get_users(db=db)
    if not users:
        raise _fastapi.HTTPException(status_code=404, detail="NO USERS TO DISPLAY")
    return users

@router.post("/",response_model = _schemas.User)
def create_user(
    user: _schemas.UserCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    user = _services.add_users(user=user, db=db)
    if not user:
        raise _fastapi.HTTPException(status_code=404, detail="NO USERS TO DISPLAY")
    return user
