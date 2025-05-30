from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import get_async_session

router = APIRouter()

@router.get("/", response_model=list[schemas.Topic])
async def read_topics(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_topics(session)

@router.post("/", response_model=schemas.Topic)
async def create_topic(topic: schemas.TopicCreate, session: AsyncSession = Depends(get_async_session)):
    return await crud.create_topic(session, topic)
