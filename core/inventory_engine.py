def compute_build_capacity(bom, stock_df):
    stock_map = dict(zip(stock_df.part_id, stock_df.quantity_available))
    capacities = {}

    for part, qty in bom.items():
        available = stock_map.get(part, 0)
        capacities[part] = available // qty if qty > 0 else 0

    min_part = min(capacities, key=capacities.get)
    return capacities[min_part], min_part, capacities
