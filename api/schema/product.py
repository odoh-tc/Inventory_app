from tortoise.contrib.pydantic import pydantic_model_creator
from models import Product




product_pydantic = pydantic_model_creator(Product, name="Product")
product_pydanticIn = pydantic_model_creator(Product, name="ProductIn", exclude_readonly=True)