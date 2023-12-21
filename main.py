# import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get("/blog")
async def index(limit=10, published: bool = True, sort: str | None = None):
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}


@app.get("/blog/unpublished")
async def unpublished():
    return {"data": "all unpublished blog"}


@app.get("/blog/{id}")
async def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
async def comments(id: int, limit=10):
    return {"data": ["1", "2"]}


class Blog(BaseModel):
    title: str
    body: str
    published: bool | None


@app.post("/blog")
async def create_blog(blog: Blog):
    return {"data": f"Blog is created with title as {blog.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
