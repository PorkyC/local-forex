import json
from datetime import datetime, timedelta

class LocalForex:
    def __init__(self):
        self.data = json.load(open("local_forex/rate_data.json", "r"))
        self.symbols = self.data.keys()

class ForexRates(LocalForex):
    def get_name(self, symbol):
        return self.data[symbol]['name']
    
    def get_label(self, symbol):
        return self.data[symbol]['label']
    
    def check_symbol(self, symbol):
        return True if symbol in self.symbols else False

    def get_rate(self, symbol, date=datetime.today()):
        symbol = symbol.lower()
        if not self.check_symbol(symbol):
            return None
        if symbol == "cad":
            return 1
        date_str = date.strftime("%Y-%m-%d")
        print(date_str)
        try:
            return float(self.data[symbol]['rates'][date.strftime("%Y-%m-%d")])
        except KeyError:
            return self.get_rate(symbol, date - timedelta(days=1))
    
    # get_rate returns the rate given a base/quote (quote defaults to cad) symbol pair on a given date
    # If no date is given, the most recent rate is returned used
    def get_conversion_rate(self, base, quote="CAD", date=datetime.today()):
        quote_rate = self.get_rate(quote, date)
        base_rate = self.get_rate(base, date)
        return base_rate / quote_rate

    