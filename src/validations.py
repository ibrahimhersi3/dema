# src/validations.py
from pydantic import BaseModel, ValidationError
from typing import Optional, Union
import math

class Order(BaseModel):
    orderId: str
    productId: str
    currency: str
    quantity: int
    shippingCost: float
    amount: float
    channel: str
    channelGroup: str
    campaign: Optional[Union[str, float]] = None
    dateTime: str

class Inventory(BaseModel):
    productId: str
    name: str
    quantity: int
    category: str
    subCategory: str

def validate_order_record(record: dict) -> dict:
    try:
        order = Order(**record)
        return order.dict()
    except ValidationError as e:
        print(f"Order validation error: {e}")
        return None

def validate_inventory_record(record: dict) -> dict:
    try:
        inventory = Inventory(**record)
        return inventory.dict()
    except ValidationError as e:
        print(f"Inventory validation error: {e}")
        return None
