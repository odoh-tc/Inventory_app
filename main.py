from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from router.supplier import supplier_router
from router.product import product_router


app = FastAPI()

app.include_router(supplier_router)
app.include_router(product_router)

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