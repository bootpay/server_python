import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.BootpayApi import BootpayApi

bootpay = BootpayApi('59bfc738e13f337dbd6ca48a', 'pDc0NwlkEX3aSaHTp/PPL/i8vn5E/CqRChgyEp/gHD0=')

result = bootpay.get_access_token()
if result['status'] is 200:
    print(bootpay.subscribe_billing_reserve(
        '5b025b33e13f33310ce56fb',
        '정기 결제 테스트 아이템',
        3000,
        '12345',
        time.time() + 10,
        'https://dev-api.bootpay.co.kr/callback')
    )
