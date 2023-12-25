from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blog
from .. import schemas


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)


@router.get("/", response_model=list[schemas.ShowBlog])
async def all(db: Session = Depends(get_db)):
    return await blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return await blog.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id: int, db: Session = Depends(get_db)):
    return await blog.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return await blog.update(id, request, db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlog,
)
async def show(id: int, db: Session = Depends(get_db)):
    return await blog.show(id, db)
