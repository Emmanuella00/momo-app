#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import json
import re

tree = ET.parse("modified_sms_v2.xml")
root = tree.getroot()

sms_records = []

for sms in root.findall("sms"):
    body = sms.get("body", "")

    amount_match = re.search(r"([0-9,]+)\s*RWF", body)
    amount = float(amount_match.group(1).replace(",", "")) if amount_match else 0.0

    sender_match = re.search(r"from\s+([A-Za-z\s]+)\s", body)
    sender = sender = sender_match.group(1).strip() if sender_match else "self"

    receiver_match = re.search(r"to\s+([A-Za-z\s]+)\s", body)
    receiver = receiver_match.group(1).strip() if receiver_match else "self"


    record = {
        "transaction_type": sms.get("type"),
        "amount": amount,
        "sender": sender,
        "receiver": receiver,
        "timestamp": sms.get("readable_date"),
        "body": body
    }
    sms_records.append(record)

json_output = json.dumps(sms_records, indent=2)

with open("sms_records.json", "w") as f:
    f.write(json_output)

print("Parsed", len(sms_records), "records")


