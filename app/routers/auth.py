import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm

from fastapi import APIRouter
from app.services import users as _user
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
    user = await _user.authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise _fastapi.HTTPException(status_code=401, detail="Invalid Credentials")

    return await _user.create_token(user)