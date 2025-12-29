import os
import re

def parse_emails(email_folder="data/emails"):
    events = []

    for file in os.listdir(email_folder):
        path = os.path.join(email_folder, file)
        with open(path, "r", errors="ignore") as f:
            text = f.read().lower()

        if "delay" in text or "postponed" in text:
            events.append({
                "type": "SUPPLIER_DELAY",
                "severity": "HIGH",
                "message": "Supplier delivery delay detected"
            })

        if "price increase" in text or "price hike" in text:
            events.append({
                "type": "PRICE_INCREASE",
                "severity": "MEDIUM",
                "message": "Supplier price increase announced"
            })

        if "partial" in text or "shortage" in text:
            events.append({
                "type": "PART_SHORTAGE",
                "severity": "HIGH",
                "message": "Supplier cannot fulfill full quantity"
            })

        if "new version" in text or "engineering change" in text:
            events.append({
                "type": "ENGINEERING_CHANGE",
                "severity": "MEDIUM",
                "message": "Engineering change may obsolete existing parts"
            })

        if "cancel" in text:
            events.append({
                "type": "ORDER_CANCELLATION",
                "severity": "HIGH",
                "message": "Purchase order cancellation detected"
            })

    return events
