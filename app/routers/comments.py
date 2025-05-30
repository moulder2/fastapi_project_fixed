from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import get_async_session

router = APIRouter()

@router.get("/", response_model=list[schemas.Comment])
async def read_comments(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_comments(session)

@router.post("/", response_model=schemas.Comment)
async def create_comment(comment: schemas.CommentCreate, session: AsyncSession = Depends(get_async_session)):
    return await crud.create_comment(session, comment)