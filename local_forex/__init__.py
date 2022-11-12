from local_forex import ForexRates

forex_dict = ForexRates()
print(forex_dict.get_rate("uSd"))
print(forex_dict.get_conversion_rate("CAD", "USD"))
boc_rates_json = forex_dict.fetch_boc_rates()
forex_dict.update_boc_rates(boc_rates_json)