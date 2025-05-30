from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import get_async_session

router = APIRouter()

@router.get("/")
async def read_posts(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_posts(session)

@router.post("/", response_model=schemas.Post)
async def create_post(post: schemas.PostCreate, session: AsyncSession = Depends(get_async_session)):
    return await crud.create_post(session, post)

@router.put("/{post_id}")
async def update_post(post_id: int, post: schemas.PostUpdate, session: AsyncSession = Depends(get_async_session)):
    await crud.update_post(session, post_id, post)
    return {"message": "Post updated"}

@router.delete("/{post_id}")
async def delete_post(post_id: int, session: AsyncSession = Depends(get_async_session)):
    await crud.delete_post(session, post_id)
    return {"message": "Post deleted"}