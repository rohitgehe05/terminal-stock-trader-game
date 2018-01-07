import requests
from prettytable import PrettyTable
from pprint import pprint


class Lookup:

    def __init__(self):
        self.lookup_url = 'http://dev.markitondemand.com/Api/v2/Lookup/json?input='
        self.quote_url = 'http://dev.markitondemand.com/Api/v2/Quote/json?symbol='
        self.base_url = 'https://api.coinmarketcap.com/v1/ticker/'

    def company_search(self, string):
        search = requests.get(self.lookup_url + string)
        try:
            return search.json()[0]
        except:
            return 0

    def get_quote(self, string):
        search = requests.get(self.quote_url + string)
        try:
            return search.json().get('LastPrice')
        except ValueError:
            return 0

    def get_details(self, string):
        search = requests.get(self.quote_url + string)
        try:
            return search.json()
        except ValueError:
            return 0

    def crypto_search(self, string):
        try:
            search = requests.get(self.base_url + string + '/?convert=USD')
            return search.json()[0]
        except:
            pass

    def crypto_price(self, string):
        try:
            search = requests.get(self.base_url + string + '/?convert=USD')
            return search.json()[0].get('price_usd')
        except:
            pass
