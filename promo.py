from typing import Callable, List
from order import Order

Promotion = Callable[[Order], float]

def promotion(promo: Promotion) -> Promotion:
    """Decorator to register a promotion function."""
    promos.append(promo)
    return promo

promos: List[Promotion] = []

@promotion
def fidelity(order: Order) -> float:
    """5% discount for customers with 1000 or more fidelity points."""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order: Order) -> float:
    """10% discount for each LineItem with 20 or more units."""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount

@promotion
def large_order(order: Order) -> float:
    """7% discount for orders with 10 or more distinct items."""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0

def best_promo(order: Order) -> float:
    """Select best discount available."""
    return max(promo(order) for promo in promos)