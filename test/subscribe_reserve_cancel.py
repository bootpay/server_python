import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.BootpayApi import BootpayApi

bootpay = BootpayApi('59bfc738e13f337dbd6ca48a', 'pDc0NwlkEX3aSaHTp/PPL/i8vn5E/CqRChgyEp/gHD0=', 'development')

result = bootpay.get_access_token()
if result['status'] is 200:
    reserve_result = bootpay.subscribe_billing_reserve(
        '5e8d3c6f05df0f036ad43e41',
        '정기 결제 테스트 아이템',
        3000,
        '12345',
        time.time() + 1000,
        'https://dev-api.bootpay.co.kr/callback'
    )
    print(reserve_result)
    if reserve_result['status'] is 200:
        response = bootpay.subscribe_billing_reserve_cancel(reserve_result['data']['reserve_id'])
        if response['status'] is 200:
            print(response)
