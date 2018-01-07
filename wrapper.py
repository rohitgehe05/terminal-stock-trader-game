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
            return search.json()
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

# q = Lookup()
# x = PrettyTable()
# x.field_names = q.crypto_search('bitcoin').keys()
# x.add_row(q.crypto_search('bitcoin').values())
# print(x.get_string(fields=["name", "symbol", "price_usd", "price_btc",
#                            "market_cap_usd", "24h_volume_usd", "percent_change_24h", "percent_change_7d"]))
# pprint(q.get_details('msft'))
# x.field_names = q.get_details('msft').keys()
# x.add_row(q.get_details('msft').values())
# print(x.get_string(fields=["Name", "Symbol", "LastPrice", "Change",
#                            "ChangePercent", "ChangeYTD", "ChangePercentYTD", "Volume"]))
