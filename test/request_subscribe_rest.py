import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.BootpayApi import BootpayApi

bootpay = BootpayApi(
    '59b731f084382614ebf72215',
    'WwDv0UjfwFa04wYG0LJZZv1xwraQnlhnHE375n52X0U='
)

result = bootpay.get_access_token()
if result['status'] is 200:
    response = bootpay.get_subscribe_billing_key(
        'nicepay',
        str(time.time()),
        '30일 결제권',
        '[ 카드 번호 ]',
        '[ 카드 비밀번호 앞자리 2개 ]',
        '[ 카드 만료 연도 2자리 ]',
        '[ 카드 만료 월 2자리 ]',
        '[ 카드 소유주 생년월일 혹은 사업자 등록번호 ]'
    )
    print(response)

    # Billing key를 취소할 때 쓰는 API
    print(
        bootpay.destroy_subscribe_billing_key(result['data']['billing_key'])
    )
