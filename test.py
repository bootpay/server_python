from lib.BootpayApi import BootpayApi
# import requests

api = BootpayApi("5b9f51264457636ab9a07cde", 'sfilSOSVakw+PZA+PRux4Iuwm7a//9CXXudCq9TMDHk=', 'development')
payload = {
    'price': 1000,
    'name': "pg test",
    'pg': 'inicis',
    'method': 'card',
    'application_id': '5b9f51264457636ab9a07cde',
    'show_agree_window': 0,
    'sms_payload': {},

    'order_id': 'order_id_1234',
    'params': {
        'callback1': 'return value 1',
        'callback2': 'return value 2',
        'customvar1234': 'custom value 1234'
    }
}

result = api.remote_link(payload)
print(result)


# print api.confirm('593f8febe13f332431a8ddae').text
# print api.cancel('593f8febe13f332431a8ddae', 'name', 'reason').text
