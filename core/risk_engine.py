from core.bom_engine import load_bom

def detect_risks(stock_df, dispatch_df, email_events):
    risks = []
    bom = load_bom()["S2_V2_PRO"]

    part_col = "part_id"
    stock_col = "quantity_available"
    safety_col = "min_stock_level"

    stock = dict(zip(stock_df[part_col], stock_df[stock_col]))
    safety = dict(zip(dispatch_df[part_col], dispatch_df[safety_col]))

    for part, qty in stock.items():
        if part in safety and qty < safety[part]:
            impact = (safety[part] - qty)
            risks.append({
                "type": "LOW_STOCK",
                "part": part,
                "severity": "HIGH",
                "message": f"{part} below minimum stock",
                "impact": f"{impact} units short"
            })

    
    for event in email_events:
        if event["type"] == "SUPPLIER_DELAY":
            risks.append({
                "type": "SUPPLIER_DELAY",
                "severity": "HIGH",
                "message": event["message"],
                "impact": "Production schedule and customer deliveries at risk"
            })

        if event["type"] == "PRICE_INCREASE":
            risks.append({
                "type": "PRICE_INCREASE",
                "severity": "MEDIUM",
                "message": event["message"],
                "impact": "Cost increase – renegotiation recommended"
            })

        if event["type"] == "ENGINEERING_CHANGE":
            risks.append({
                "type": "ENGINEERING_CHANGE",
                "severity": "MEDIUM",
                "message": event["message"],
                "impact": "Existing inventory may become obsolete"
            })

    
    
    for event in email_events:
        if event["type"] == "delay":
            risks.append({
                "type": "SUPPLIER_DELAY",
                "severity": "HIGH",
                "message": "Supplier delivery delay detected",
                "impact": "Production schedule at risk"
            })

    if not risks:
        risks.append({
            "type": "OK",
            "severity": "LOW",
            "message": "No immediate operational risks",
            "impact": "All systems stable"
        })

    return risks


