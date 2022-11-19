# local-forex
A free python package to help get started in building and interacting with a local database of currency exchange rates.

## Dictionary based currency exchange rate package
* Rates provided by Bank of Canada. Includes function for fetching and saving latest rates using BoC API
* Offline JSON historical database reduces reliance on external API availability
* ~24 modern currencies supported
## Installation
```shell
pip install local-forex
cd local-forex
pip install -r requirements.txt
```

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
