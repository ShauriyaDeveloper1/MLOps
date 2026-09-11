"Is this order usable?"


def is_valid_order(order):
    "True if the order passes every rule."
    # TODO: write the four checks, return False when one fails
    return (
        order["distance_km"] > 0
        and order["prep_time_min"] > 0
        and order["traffic_level"] in (1, 2, 3)
        and order["rain"] in (0, 1)
    )
