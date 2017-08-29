from lib.BootpayApi import BootpayApi

api = BootpayApi("application_id_value_1234", '593f8febe13f332431a8ddaw')
print api.confirm('593f8febe13f332431a8ddae').text
print api.cancel('593f8febe13f332431a8ddae', 'name', 'reason').text
