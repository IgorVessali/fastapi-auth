import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm

from fastapi import APIRouter, status
from app.services import auth as _services
from app.schemas import auth as _schemas
from .. import database as _database


router = APIRouter(
    prefix="/auth",
    tags=['Autenticação']
)

@router.post("/token")
async def generate_token(
    form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends(),
    db: _orm.Session = _fastapi.Depends(_database.get_db),
):
    user = await _services.authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise _fastapi.HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials.")

    return await _services.create_token(user)


@router.post("/user")
async def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)
):
    db_user = await _services.get_user_by_email(user.email, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already in use.")

    user = await _services.create_user(user, db)

    return await _services.create_token(user)



@router.get("/user/logged", response_model=_schemas.User)
async def get_user(user: _schemas.User = _fastapi.Depends(_services.get_current_user)):
    return user