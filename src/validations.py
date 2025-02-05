# src/validations.py

from pydantic import BaseModel, ValidationError
from typing import Optional

class Order(BaseModel):
    orderId: str
    productId: str
    currency: str
    quantity: int
    shippingCost: float
    amount: float
    channel: str
    channelGroup: str
    campaign: Optional[str] = None
    dateTime: str

class Inventory(BaseModel):
    productId: str
    name: str
    quantity: int
    category: str
    subCategory: str

if __name__ == "__main__":
    # Example order validation
    sample_order = {
        "orderId": "O1",
        "productId": "prod1520#XYZ",
        "currency": "SEK",
        "quantity": 1,
        "shippingCost": 0.0,
        "amount": 100,
        "channel": "direct",
        "channelGroup": "sem",
        "campaign": None,
        "dateTime": "2023-02-01T17:12:52Z"
    }

    try:
        order = Order(**sample_order)
        print("Validated order:", order)
    except ValidationError as e:
        print("Validation error:", e)
