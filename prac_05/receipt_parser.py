import re
import json


def parse_receipt(text):
    result = {}

    # Extract all prices
    price_pattern = r'\d{1,3}(?: \d{3})*,\d{2}'
    prices = re.findall(price_pattern, text)
    result["prices"] = prices

    # Extract product names
    product_pattern = r'\d+\.\n(.+)'
    products = re.findall(product_pattern, text)
    result["products"] = [p.strip() for p in products]

    # Extract total amount
    total_match = re.search(r'ИТОГО:\n([\d\s,]+)', text)
    if total_match:
        result["total"] = total_match.group(1).strip()

    # Extract date and time
    datetime_match = re.search(r'Время:\s*([\d\.]+\s[\d:]+)', text)
    if datetime_match:
        result["datetime"] = datetime_match.group(1)

    # Extract payment method
    payment_match = re.search(r'(Банковская карта)', text)
    if payment_match:
        result["payment_method"] = payment_match.group(1)

    # Extract item details (name + price)
    items = []
    item_pattern = r'\d+\.\n(.+?)\n[\d, x]+\n([\d\s,]+)'
    
    matches = re.findall(item_pattern, text, re.DOTALL)
    
    for name, price in matches:
        items.append({
            "name": name.strip(),
            "price": price.strip()
        })

    result["items"] = items

    return result



# MAIN
if __name__ == "__main__":
    with open("raw.txt", "r", encoding="utf-8") as file:
        receipt_text = file.read()

    parsed_data = parse_receipt(receipt_text)

    print(json.dumps(parsed_data, indent=4, ensure_ascii=False))