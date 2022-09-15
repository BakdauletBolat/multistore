
from dataclasses import dataclass
from typing import Optional

@dataclass
class OrderCreateDto:
    user_id:int
    status_id:int
    payment_method_id:int
    delivery_method_id:int
    comment:Optional[str] = None
    operation_id: Optional[int] = None
    shipping_address:Optional[str] = None
    billing_address:Optional[str] = None
    store_id:Optional[str] = None
