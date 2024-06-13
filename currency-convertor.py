import requests

def get_exchange_rate(from_currency, to_currency):
    """Function to get exhange rate from one currency to another"""
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    data = response.json()
    return data["rates"].get(to_currency, None)

def convert_currency(amount, from_currency, to_currency):
    """Function to convert currency"""
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        return amount * rate
    else:
        return None

# User Interatction
from_currency = input("Enter the currency you have (e.g., USD): ").upper()
to_currency = input("Enter the currency you want (e.g., EUR): ").upper()
amount = float(input("Enter the amount to convert: "))

converted_amount = convert_currency(amount, from_currency, to_currency)
if converted_amount:
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
else:
    print("Invalid currency code.")