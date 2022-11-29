import json
from datetime import datetime, timedelta
import requests
import pathlib

PATH = str(pathlib.Path(__file__).parent.resolve())

class ForexData:
    def __init__(self):
        self.data = self.load_rates_from_file()
        self.symbols = self.data.keys()
    
    # load_rates_from_file loads the data dictionary from a json file
    def load_rates_from_file(self):
        return json.load(open(PATH + "/rate_data.json", "r"))
    
    # save_rates_to_file saves the data dictionary to a json file
    def save_rates_to_file(self):
        json.dump(self.data, open(PATH + "/rate_data.json", "w"), indent=4)

    # fetch_boc_rates returns the latest exchange rates in json format from the Bank of Canada website
    def fetch_boc_rates(self):
        # Fetch the latest exchange rates from the Bank of Canada website
        url = "https://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/json"
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # update_from_boc_rates takes the json data from the Bank of Canada website and updates the rates in the data dictionary
    def update_from_boc_rates(self, data):
        up_to_date = False
        i = -1
        while not up_to_date:
            date = data['observations'][i]['d']
            for key, value in data['observations'][i].items():
                if key != 'd':
                    symbol = key.lower()[2:5]
                    if self.data[symbol]['rates'].get(date) is None:
                        self.data[symbol]['rates'][date] = str(value['v'])
                        i -= 1
                    else:
                        up_to_date = True

class ForexRates(ForexData):
    # get_rate returns the rate given a symbol on a given date relative to CAD
    # If a rate is not available on the given date, it will return the first available rate prior to that date 
    def get_rate(self, symbol, date=datetime.today()):
        if date < datetime.strptime("2017-01-03", "%Y-%m-%d"):
            date = datetime.today()
        symbol = symbol.lower()
        if not self.check_symbol(symbol):
            return None
        if symbol == "cad":
            return 1
        rate = self.data[symbol]['rates'].get(date.strftime("%Y-%m-%d"))
        if rate:
            return float(rate)
        return self.get_rate(symbol, date - timedelta(days=1))

    def check_symbol(self, symbol):
        return True if symbol in self.symbols else False

    # get_conversion_rate returns the conversion rate between two symbols on a given date
    def get_conversion_rate(self, base, quote="CAD", date=datetime.today()):
        quote_rate = self.get_rate(quote, date)
        base_rate = self.get_rate(base, date)
        return base_rate / quote_rate
