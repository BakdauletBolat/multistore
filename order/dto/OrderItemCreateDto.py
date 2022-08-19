from dataclasses import dataclass

@dataclass
class OrderItemCreateDto:
    product_id:int
    order_id:int
    quantity:int
    cost:int