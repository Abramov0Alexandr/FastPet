from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "It's alive"}


@app.get("/{name}")
async def named_root(name):
    return {"message": name}
