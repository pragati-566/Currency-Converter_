# Fixed exchange rates (as of July 2025 - you can change them)
rates = {
    'USD': {'INR': 83.2, 'EUR': 0.91, 'GBP': 0.78},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0094},
    'EUR': {'USD': 1.1, 'INR': 91.3, 'GBP': 0.86},
    'GBP': {'USD': 1.28, 'INR': 108.6, 'EUR': 1.16}
}

print("💱 Welcome to the Currency Converter!\n")
print("Supported currencies: USD, INR, EUR, GBP\n")

from_currency = input("Enter FROM currency: ").upper()
to_currency = input("Enter TO currency: ").upper()

if from_currency not in rates or to_currency not in rates[from_currency]:
    print("❌ Conversion for given currency pair not available.")
else:
    amount_str = input(f"Enter amount in {from_currency}: ")

    if not amount_str.replace('.', '', 1).isdigit():
        print("❗ Please enter a valid numeric amount.")
    else:
        amount = float(amount_str)
        converted = amount * rates[from_currency][to_currency]
        print(f"✅ {amount} {from_currency} = {round(converted, 2)} {to_currency}")
