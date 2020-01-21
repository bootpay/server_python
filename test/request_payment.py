import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.BootpayApi import BootpayApi

bootpay = BootpayApi('59bfc738e13f337dbd6ca48a', 'pDc0NwlkEX3aSaHTp/PPL/i8vn5E/CqRChgyEp/gHD0=', 'development')

result = bootpay.get_access_token()
print(result)
if result['status'] is 200:
    print(bootpay.request_payment({
        'pg': 'kcp',
        'method': 'card',
        'order_id': str(time.time()),
        'price': 1000,
        'name': '테스트 부트페이 상품',
        'return_url': 'https://dev-api.bootpay.co.kr/callback',
        'extra': {
            'expire': 30
        }
    }))
