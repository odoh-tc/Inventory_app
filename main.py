from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()



@app.get('/')
def home():
    return {"Welcome to our home page"}


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)