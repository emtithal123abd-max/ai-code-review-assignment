#  corrected implementation for Task 1.
def calculate_average_order_value(orders):
    total = 0.0
    valid_orders_count = 0 

    for order in orders:
        if order.get("status", "cancelled") != "cancelled":
            amount = order.get("amount")
            if amount is None:
                continue

            total += float(amount)
            valid_orders_count += 1

    return total / valid_orders_count if valid_orders_count else 0.0
