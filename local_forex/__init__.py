from local_forex import ForexRates

forex_dict = ForexRates()
print(forex_dict.get_rate("usd"))
print(forex_dict.get_rate("USD", "CAD"))