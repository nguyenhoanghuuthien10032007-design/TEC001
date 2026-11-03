import re
def redact_phone_numbers(document: str) -> str:
    pattern = r"\+84\d+|\b\d{10}\b"
    return re.sub(pattern, "[REDACTED]",document)
doc = "Call me at +84902301473 or 0123456789 for support."
print(redact_phone_numbers(doc))
