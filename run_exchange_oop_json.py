from exchange_oop_json import RatesPasser

rates_obj = RatesPasser('exchange_rate.json')

for key in rates_obj.rates:

    print(key, rates_obj.rates[key])