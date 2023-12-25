from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import user
from .. import schemas


router = APIRouter(
    prefix="/user",
    tags=["Users"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowUser,
)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return await user.create(request, db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowUser,
)
async def get_user(id: int, db: Session = Depends(get_db)):
    return await user.show(id, db)
