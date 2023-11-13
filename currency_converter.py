# currency_converter.py

exchange_rates = {
    'USD': 1,
    'EUR': 0.85,
    'JPY': 110.53,
}

def convert_currency(amount, from_currency, to_currency):
   
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    
    if from_currency in exchange_rates and to_currency in exchange_rates:
        
        rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        return amount * rate
    else:
        
        raise ValueError(f"No exchange rate for {from_currency} to {to_currency}")
