import currency_converter as cc

try:
    converted_amount = cc.convert_currency(100, 'USD', 'EUR')
    print(f"Converted amount: €{converted_amount}")
except ValueError as e:
    print(e)
