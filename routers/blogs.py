from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import Optional
from database import SessionLocal
from models import Blog
from schemas import BlogCreate, BlogUpdate, BlogResponse

router = APIRouter(prefix="/blogs", tags=["blogs"])


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[BlogResponse])
def list_blogs(
        published: Optional[bool] = Query(None, description="Filter by publication status"),
        db: Session = Depends(get_db),
):
    query = db.query(Blog)
    if published is not None:
        query = query.filter(Blog.is_published == published)
    return query.all()


@router.get("/{id}", response_model=BlogResponse)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


@router.post("/", response_model=BlogResponse, status_code=status.HTTP_201_CREATED)
def update_blog(blog_data: BlogCreate, db: Session = Depends(get_db)):
    new_blog = Blog(**blog_data.model_dump())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.put("/{id}", response_model=BlogResponse)
def update_blog(blog_id: int, update_data: BlogUpdate, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    if update_data.title is not None:
        blog.title = update_data.title
    if update_data.description is not None:
        blog.description = update_data.description

    db.commit()
    db.refresh(blog)
    return blog


@router.patch("/{id}/publish", response_model=BlogResponse)
def toggle_publish(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    blog.is_published = not blog.is_published
    db.commit()
    db.refresh(blog)
    return blog


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    db.delete(blog)
    db.commit()
    return
