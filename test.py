from lib.BootpayApi import BootpayApi
# import requests
# import json


api = BootpayApi("5b9f51264457636ab9a07cde", 'sfilSOSVakw+PZA+PRux4Iuwm7a//9CXXudCq9TMDHk=', 'development')
# api = BootpayApi("5b8f6a4d396fa665fdc2b5ea", 'n9jO7MxVFor3o//c9X5tdep95ZjdaiDvVB4h1B5cMHQ=')

payload = {
    'price': 1000,
    'name': "pg test",
    'pg': 'inicis',
    'method': 'card',
#     'application_id': '5b8f6a4d396fa665fdc2b5ea',
    'application_id': '5b9f51264457636ab9a07cde',
    'show_agree_window': 0,
    'items': json.dumps([
                {
                    'item_name': 'i am item',
                    'qty': 1,
                    'unique': '123',
                    'price': 1000,
                    'cat1': 'TOP',
                    'cat2': 'T-Shirt',
                    'cat3': 'round T',
                }
    ]),
    'user_info': json.dumps({
        'username': 'user name',
        'email': 'user email',
        'addr': 'user address',
        'phone': '010-1234-4567'
    }),
    'order_id': 'order_id_1234',
    'params': json.dumps({
        'callback1': 'return value 1',
        'callback2': 'return value 2',
        'customvar1234': 'custom value 1234'
    })
}


result = api.remote_link(payload)
print(result)
