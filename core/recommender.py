def recommend(risks):
    actions = []

    for r in risks:
        if r["type"] == "SUPPLIER_DELAY":
            actions.append("Expedite alternative supplier or delay sales commitments")

        if r["type"] == "PRICE_INCREASE":
            actions.append("Trigger supplier renegotiation or evaluate alternates")

        if r["type"] == "ENGINEERING_CHANGE":
            actions.append("Use existing inventory before reordering or return excess stock")

        if r["type"] == "LOW_STOCK":
            actions.append(f"Increase minimum stock for {r['part']}")

    if not actions:
        actions.append("No action required")

    return list(set(actions))
