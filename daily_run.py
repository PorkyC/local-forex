from datetime import datetime

from local_forex import ForexData

fx = ForexData()
fx.update_from_boc_rates(fx.fetch_boc_rates())
fx.save_rates_to_file()
print(datetime.now(), "Rates fetched and saved.")