# local-forex

## Dictionary based currency exchange rate package
* Written in Python
* Rates provided by Bank of Canada. Includes function for fetching and saving latest rates using BoC API
* Offline JSON historical database reduces reliance on external API availabilility
* ~24 modern currencies supported

## Example conversion
```python
import local_forex

fx = local_forex.ForexRates()

# Example conversion rate query for USD/EUR on December 02, 2015
from datetime import datetime
rate = local_forex.get_conversion_rate(base="USD", quote="EUR", date=datetime(2015,12,02))

```
## Fetching and saving latest rates
```python
latest_rates = fx.fetch_boc_rates()
fx.update_from_boc_rates(latest_rates)
fx.save_rates_to_file()
```
