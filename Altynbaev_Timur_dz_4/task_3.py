from requests import get, utils
from datetime import datetime

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
unicode = utils.get_unicode_from_response(response)


def currency_rates(currency):
    content = unicode.split("<Valute ID=")
    for i in content:
        if currency.upper() in i:
            print(datetime.now(tz=None))
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


print(currency_rates(input("Введите код валюты: ")))
print(currency_rates("usd"))
print(currency_rates("eur"))