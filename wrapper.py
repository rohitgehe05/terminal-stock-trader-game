import requests


class Lookup:

    def __init__(self):
        self.lookup_url = 'http://dev.markitondemand.com/Api/v2/Lookup/json?input='
        self.quote_url = 'http://dev.markitondemand.com/Api/v2/Quote/json?symbol='
        self.base_url = 'https://api.coinmarketcap.com/v1/ticker/'

    def company_search(self, string):
        search = requests.get(self.lookup_url + string)
        try:
            return search.json()
        except:
            return 0

    def get_quote(self, string):
        search = requests.get(self.quote_url + string)
        try:
            return search.json().get('LastPrice')
        except ValueError:
            return 0

    def crypto_search(self, string):
        try:
            search = requests.get(self.base_url + string + '/?convert=USD')
            return search.json()
        except:
            pass

    def crypto_price(self, string):
        try:
            search = requests.get(self.base_url + string + '/?convert=USD')
            return search.json()[0].get('price_usd')
        except:
            pass

# m = Lookup()
# print(m.company_search('aapl'))
# print(m.get_quote('aapl'))

# c = Lookup()
# print(c.crypto_search('bitcoin'))
# print(c.crypto_price('bitcoin'))
