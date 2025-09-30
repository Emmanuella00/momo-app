#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import json
import re
from datetime import datetime

TYPE_MAP = {"1": "CREDIT", "2": "DEBIT"}

def parse_sms_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    sms_records = []

    for i, sms in enumerate(root.findall("sms"), start=1):
        body = sms.get("body", "")

        amount_match = re.search(r"([0-9,]+)\s*RWF", body)
        amount = float(amount_match.group(1).replace(",", "")) if amount_match else 0.0

        sender_match = re.search(r"from\s+([A-Za-z0-9\s]+)", body)
        sender = sender_match.group(1).strip() if sender_match else "self"

        receiver_match = re.search(r"to\s+([A-Za-z0-9\s]+)", body)
        receiver = receiver_match.group(1).strip() if receiver_match else "self"

        raw_date = sms.get("readable_date", "")
        try:
            parsed_date = datetime.strptime(raw_date, "%d %b %Y %I:%M:%S %p")
            iso_date = parsed_date.isoformat()
        except:
            iso_date = raw_date

        record = {
            "id": i,
            "transaction_type": TYPE_MAP.get(sms.get("type"), "UNKNOWN"),
            "amount": amount,
            "sender": sender,
            "receiver": receiver,
            "timestamp": iso_date,
            "readable_timestamp": raw_date,
            "body": body
        }
        sms_records.append(record)

    return sms_records


if __name__ == "__main__":
    records = parse_sms_xml("modified_sms_v2.xml")

    with open("sms_records.json", "w") as f:
        json.dump(records, f, indent=2)

    print(f"Parsed {len(records)} records → saved to sms_records.json")
