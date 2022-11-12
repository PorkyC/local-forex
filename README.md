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

# Example conversion rate query for USD/EUR on December 02, 2020
from datetime import datetime
rate = local_forex.get_conversion_rate(base="USD", quote="EUR", date=datetime(2020,12,02))

```
## Backfilling rates
* backfill.py is included for convenience. Run Mon-Fri after 16:30EST to update database daily (e.g. Launchd on MacOS).
```python
online_rates = fx.fetch_boc_rates()
fx.update_from_boc_rates(online_rates)
fx.save_rates_to_file()
```
