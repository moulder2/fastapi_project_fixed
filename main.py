from fastapi import FastAPI
import app.routers.posts as posts
import app.routers.topics as topics
import app.routers.comments as comments

app = FastAPI(title="Blog API")

app.include_router(posts.router, prefix="/posts")
app.include_router(topics.router, prefix="/topics")
app.include_router(comments.router, prefix="/comments")