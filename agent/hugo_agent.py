from core.bom_engine import load_bom
from core.inventory_engine import compute_build_capacity
from core.email_parser import parse_emails
from core.risk_engine import detect_risks
from core.recommender import recommend

def hugo_answer(question, data):
    q = question.lower()

    bom = load_bom()["S2_V2_PRO"]
    stock = data["stock"]
    dispatch = data["dispatch"]

    emails = parse_emails()
    risks = detect_risks(stock, dispatch, emails)

    if any(k in q for k in ["build", "capacity", "how many"]):
        qty, bottleneck, _ = compute_build_capacity(bom, stock)
        return (
            f"Build Capacity Report\n"
            f"- Max scooters buildable: {qty}\n"
            f"- Bottleneck part: {bottleneck}"
        )

    if any(k in q for k in ["risk", "urgent", "attention", "problem"]):
        response = "Active Risks Detected:\n"
        for r in risks:
            response += (
                f"- [{r['severity']}] {r['message']} | Impact: {r['impact']}\n"
            )
        return response

    if any(k in q for k in ["optimize", "dispatch", "inventory", "reorder"]):
        actions = recommend(risks)
        return (
            "Inventory Optimization Suggestions:\n"
            + "\n".join(f"- {a}" for a in actions)
        )

    if any(k in q for k in ["summary", "dashboard", "status"]):
        return (
            "Daily Operations Summary\n"
            f"- Active risks: {len(risks)}\n"
            f"- Immediate actions recommended: {len(recommend(risks))}\n"
            "- Hugo is actively monitoring suppliers and inventory"
        )

    return (
        "I can help with:\n"
        "• Build capacity\n"
        "• Risk detection\n"
        "• Inventory optimization\n"
        "• Daily operational summary\n\n"
        "Try asking:\n"
        "- Which parts need urgent attention?\n"
        "- Optimize inventory settings\n"
        "- Give me today’s operations summary"
    )
