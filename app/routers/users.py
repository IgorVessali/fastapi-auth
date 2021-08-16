import fastapi as _fastapi
import sqlalchemy.orm as _orm

from fastapi import APIRouter
from app.services import auth as _services
from app.schemas import auth as _schemas
from .. import database as _database


router = APIRouter(
    prefix="/user",
    tags=['Usuarios']
)


# @router.post("/")
# async def create_user(
#     user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)
# ):
#     db_user = await _services.get_user_by_email(user.email, db)
#     if db_user:
#         raise _fastapi.HTTPException(status_code=400, detail="Email already in use")

#     user = await _services.create_user(user, db)

#     return await _services.create_token(user)



# @router.get("/logged", response_model=_schemas.User)
# async def get_user(user: _schemas.User = _fastapi.Depends(_services.get_current_user)):
#     return user