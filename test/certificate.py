import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.BootpayApi import BootpayApi

bootpay = BootpayApi('59bfc738e13f337dbd6ca48a', 'pDc0NwlkEX3aSaHTp/PPL/i8vn5E/CqRChgyEp/gHD0=')

result = bootpay.get_access_token()
if result['status'] is 200:
    print(bootpay.certificate('1234'))
