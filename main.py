from fastapi import FastAPI
from app.database import engine, Base
from app.routers import posts, topics, comments

app = FastAPI(title="Blog API")

app.include_router(posts.router, prefix="/posts")
app.include_router(topics.router, prefix="/topics")
app.include_router(comments.router, prefix="/comments")

# старт сервера
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)