from fastapi import APIRouter, Depends, HTTPException, Query, status
from schema.product import product_pydantic, product_pydanticIn, Product
from tortoise.exceptions import DoesNotExist
from schema.supplier import supplier_pydantic, supplier_pydanticIn, Supplier




product_router = APIRouter(
    prefix="/product",
    tags=["product"],
    responses={404: {"description": "Not found"}},
)


@product_router.post("/{supplier_id}/")
async def add_product(supplier_id: int, product_info: product_pydanticIn):
    supplier = await Supplier.get(id=supplier_id)
    product_info = product_info.dict(exclude_unset=True)
    product_info["revenue"] += product_info["quantity_sold"] * product_info["unit_price"]
    product_obj = await Product.create(**product_info, supplied_by = supplier)
    response = await product_pydantic.from_tortoise_orm(product_obj)
    return {
        "message": "Product added successfully",
        "data": response,
    }

@product_router.get("/")
async def get_all_product():
    response = await product_pydantic.from_queryset(Product.all())
    return {
        "data": response,
        "count": len(response),
        "message": "Product fetched successfully",
    }


@product_router.get("/{product_id}/")
async def get_specific_product(product_id: int):
    try:
        response = await product_pydantic.from_queryset_single(Product.get(id=product_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    return {
        "data": response,
        "message": "Product fetched successfully",
    }

@product_router.put("/{product_id}")
async def update_product(product_id: int, product_info: product_pydanticIn):
    try:
        product_obj = await Product.get(id=product_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found",
        )
    product_info = product_info.dict(exclude_unset=True)
    product_obj.name = product_info["name"]
    product_obj.quantity_in_stock = product_info["quantity_in_stock"]
    product_obj.revenue += (product_info["quantity_sold"] * product_info["unit_price"]) + product_info["revenue"]
    product_obj.quantity_sold = product_info["quantity_sold"]
    product_obj.unit_price = product_info["unit_price"]
    await product_obj.save()
    response = await product_pydantic.from_tortoise_orm(product_obj)
    return {
        "message": "Product updated successfully",
        "data": response,
    }

@product_router.delete("/{product_id}")
async def delete_product(product_id: int):
    try:
        product_obj = await Product.get(id=product_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found",
        )
    await product_obj.delete()
    return {
        "message": "Product deleted successfully",
    }


















