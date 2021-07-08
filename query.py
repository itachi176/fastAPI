from fastapi import FastAPI

app = FastAPI()

fake_item_db = [{"item_name": "foo"}, {"item_name": "bar"}, {"item_name": "Baz"}]

@app.get("/item/")

async def read_item(skip: int = 0, limit: int = 10):
    return fake_item_db[skip: skip + limit]
