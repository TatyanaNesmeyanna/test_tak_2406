import requests

from constants import BASE_URL

class Stores:
    @staticmethod
    def get_all_stores(self, token):
        response = requests.get(url=BASE_URL + '/api​/v1​/stores/', headers={'Authorization': 'Bearer ' + token})
        return response

    @staticmethod
    def get_sorted_stores(self, token, params):
        response = requests.get(url=BASE_URL + '/api​/v1​/stores/'+'?sort='+params, headers={'Authorization': 'Bearer ' + token})
        return response
