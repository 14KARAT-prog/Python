from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
unicode = utils.get_unicode_from_response(response)


def currency_rates(currency):
    content = unicode.split("<Valute ID=")
    for i in content:
        if currency.upper() in i:
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


if __name__ == "__main__":
    print("I'm program")
else:
    print("I'm module")
