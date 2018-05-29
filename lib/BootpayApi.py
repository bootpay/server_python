import requests


class BootpayApi:
    base_url = {
        'development': 'https://dev-api.bootpay.co.kr',
        'production': 'https://api.bootpay.co.kr'
    }

    def __init__(self, application_id, private_key, mode='production'):
        self.application_id = application_id
        self.pk = private_key
        self.mode = mode
        self.token = None

    def api_url(self, uri=None):
        if uri is None:
            uri = []
        return '/'.join([self.base_url[self.mode]] + uri)

    def get_access_token(self):
        data = {
            'application_id': self.application_id,
            'private_key': self.pk
        }
        response = requests.post(self.api_url(['request', 'token']), data=data)
        result = response.json()
        if result['status'] is 200:
            self.token = result['data']['token']
        return result

    def cancel(self, receipt_id, price=None, name=None, reason=None):
        payload = {'receipt_id': receipt_id,
                   'price': price,
                   'name': name,
                   'reason': reason}

        return requests.post(self.api_url(['cancel.json']), data=payload, headers={
            'Authorization': self.token
        }).json()

    def verify(self, receipt_id):
        return requests.get(self.api_url(['receipt', receipt_id]), headers={
            'Authorization': self.token
        }).json()

    def subscribe_billing(self, billing_key, item_name, price, order_id, items=None):
        if items is None:
            items = []
        payload = {
            'billing_key': billing_key,
            'item_name': item_name,
            'price': price,
            'order_id': order_id,
            'items': items
        }
        return requests.post(self.api_url(['subscribe', 'billing.json']), data=payload, headers={
            'Authorization': self.token
        }).json()
