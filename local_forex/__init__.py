from local_forex import ForexRates

forex_dict = ForexRates()
print(forex_dict.get_rate("uSd"))
print(forex_dict.get_conversion_rate("JPY", "cnY"))