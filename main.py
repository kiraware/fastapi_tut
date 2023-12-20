from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def index():
    return {"data": {"name": "budi"}}

@app.get("/about")
async def about():
    return {"data": "About page"}
