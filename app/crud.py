from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import update, delete
from app import models, schemas

# POST
async def get_posts(session: AsyncSession):
    result = await session.execute(select(models.Post))
    return result.scalars().all()

async def create_post(session: AsyncSession, post: schemas.PostCreate):
    new_post = models.Post(**post.dict())
    session.add(new_post)
    await session.commit()
    await session.refresh(new_post)
    return new_post

async def update_post(session: AsyncSession, post_id: int, post: schemas.PostUpdate):
    await session.execute(update(models.Post).where(models.Post.id == post_id).values(**post.dict()))
    await session.commit()

async def delete_post(session: AsyncSession, post_id: int):
    await session.execute(delete(models.Post).where(models.Post.id == post_id))
    await session.commit()

# TOPIC
async def get_topics(session: AsyncSession):
    result = await session.execute(select(models.Topic))
    return result.scalars().all()

async def create_topic(session: AsyncSession, topic: schemas.TopicCreate):
    new_topic = models.Topic(**topic.dict())
    session.add(new_topic)
    await session.commit()
    await session.refresh(new_topic)
    return new_topic

# COMMENT
async def get_comments(session: AsyncSession):
    result = await session.execute(select(models.Comment))
    return result.scalars().all()

async def create_comment(session: AsyncSession, comment: schemas.CommentCreate):
    new_comment = models.Comment(**comment.dict())
    session.add(new_comment)
    await session.commit()
    await session.refresh(new_comment)
    return new_comment