def serialize(items):
    serialized = []
    for row in items:
        serialized.extend(iter(row))

    return serialized


from hidden import north, center, south

from collections import Counter


north_counter = Counter(serialize(north))
north_total = sum(north_counter.values())
center_counter = Counter(serialize(center))
center_total = sum(center_counter.values())
new_var = Counter(serialize(south))
south_total = sum(new_var.values())

print(f"В магазине north куплено {north_total} товаров")
print(f"В магазине center куплено {center_total} товаров")
print(f"В магазине south куплено {south_total} товаров")
