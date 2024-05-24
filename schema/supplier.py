from tortoise.contrib.pydantic import pydantic_model_creator
from models import Supplier




supplier_pydantic = pydantic_model_creator(Supplier, name="Supplier")
supplier_pydanticIn = pydantic_model_creator(Supplier, name="Supplier", exclude_readonly=True)