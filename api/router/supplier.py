from fastapi import APIRouter, Depends, HTTPException, Query, status
from models import Product
from schema.supplier import supplier_pydantic, supplier_pydanticIn, Supplier
from tortoise.exceptions import DoesNotExist



supplier_router = APIRouter(
    prefix="/supplier",
    tags=["supplier"],
    responses={404: {"description": "Not found"}},
)


@supplier_router.post('/')
async def add_supplier(supplier_info: supplier_pydanticIn):
    supplier_obj = await Supplier.create(**supplier_info.dict(exclude_unset=True))
    response = await supplier_pydantic.from_tortoise_orm(supplier_obj)
    return {"status": "ok", "data" : response}



@supplier_router.get('/')
async def get_all_suppliers():
    response = await supplier_pydantic.from_queryset(Supplier.all())
    return {"status": "ok", "data": response}


@supplier_router.get("/{supplier_id}")
async def get_specific_supplier(supplier_id: int):

    response = await supplier_pydantic.from_queryset_single(Supplier.get(id=supplier_id))
    return {"status": "ok", "data": response}



@supplier_router.put("/{supplier_id}")
async def update_supplier(supplier_id: int, supplier_info: supplier_pydanticIn):
    try:
        supplier_obj = await Supplier.get(id=supplier_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Supplier with id {supplier_id} not found",
        )
    
    await supplier_obj.update_from_dict(supplier_info.dict(exclude_unset=True))
    await supplier_obj.save()
    response = await supplier_pydantic.from_tortoise_orm(supplier_obj)
    return {"status": "ok", "data": response}

@supplier_router.delete("/{supplier_id}")
async def delete_supplier(supplier_id: int):
    try:
        supplier_obj = await Supplier.get(id=supplier_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Supplier with id {supplier_id} not found",
        )
    await supplier_obj.delete()
    return {"status": "ok"}