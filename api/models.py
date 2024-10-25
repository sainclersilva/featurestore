#Definição dos Modelos com Pydantic

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Modelo para dados do Consumer
class Consumer(BaseModel):
    customer_id: str
    language: Optional[str]
    created_at: datetime
    active: int
    customer_phone_area: Optional[str]
    customer_phone_number: Optional[str]

# Modelo para dados do Restaurant
class Restaurant(BaseModel):
    id: str
    created_at: datetime
    enabled: int
    price_range: Optional[float]
    average_ticket: Optional[float]
    takeout_time: Optional[float]
    delivery_time: Optional[float]
    minimum_order_value: Optional[float]
    merchant_zip_code: Optional[str]
    merchant_city: Optional[str]
    merchant_state: Optional[str]
    merchant_country: Optional[str]
