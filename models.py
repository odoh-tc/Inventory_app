from tortoise.models import Model
from tortoise import fields



class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, nullable=False)
    quantity_in_stock = fields.IntField(default=0)
    quantity_sold = fields.IntField(default=0)
    unit_price = fields.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    revenue = fields.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    supplied_by = fields.ForeignKeyField("models.Supplier",
                                         related_name="goods_supplied")


class Supplier(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, nullable=False)
    company = fields.CharField(max_length=200)
    email = fields.CharField(max_length=100)
    phone_number = fields.CharField(max_length=20)