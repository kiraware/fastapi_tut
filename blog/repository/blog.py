from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas


async def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


async def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


async def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found",
        )

    blog.delete(synchronize_session=False)
    db.commit()
    return "done"


async def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found",
        )

    blog.update(request.model_dump())
    db.commit()
    return "updated"


async def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with the id {id} is not available"}
    return blog
