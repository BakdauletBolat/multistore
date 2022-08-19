
from dataclasses import dataclass

@dataclass
class OrderCreateDto:
    user_id:int
    status_id:int
    payment_method_id:int
    delivery_method_id:int
    comment:str = None
    shipping_address:str = None
    billing_address:str = None
    store_id:int = None
