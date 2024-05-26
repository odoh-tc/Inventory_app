from typing import List

from fastapi import APIRouter, BackgroundTasks, FastAPI
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from dotenv import dotenv_values

from models import Product, Supplier



auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

credentials = dotenv_values(".env")

class EmailSchema(BaseModel):
    email: List[EmailStr]

class EmailContent(BaseModel):
    message: str
    subject: str




conf = ConnectionConfig(
    MAIL_USERNAME =credentials["EMAIL"],
    MAIL_PASSWORD = credentials["PASS"],
    MAIL_FROM = credentials["EMAIL"],
    MAIL_PORT = 465,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

@auth_router.post("/email/{supplier_id}")
async def send_email(supplier_id: int, content: EmailContent):

    supplier = await Supplier.get(id = supplier_id)
    supplier_email = [supplier.email]

    

    html = f"""
    <h5>John Doe Business LTD</h5> 
    <br>
    <p>{content.message}</p>
    <br>
    <h6>Best Regars</p>
    <h6>John Business LTD</h6>
    """

    message = MessageSchema(
        subject=content.subject,
        recipients=supplier_email,  # List of recipients, as many as you can pass 
        body=html,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return {"status": "ok"} 