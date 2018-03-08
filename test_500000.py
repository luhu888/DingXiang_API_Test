# -*- coding: utf-8 -*-
# __author__=luhu
import hashlib
import json

import requests
import datetime
import time
now_time = int(time.mktime(datetime.datetime.now().timetuple()))
print(now_time)


def test_500000(shop_id=13, clinic_status=4, timestamp=now_time,
                doctor_id='1261', department_id='', charge_status=''):
    url = {"shopId": shop_id,
           "clinic_status": clinic_status,
           "appId": "1616499178",
           "appSignKey": "f2l9SESH9tKYsXGXPu5cZ0fk9UVCbTzhQSL0FN8uM0UJozFUOi4fEFhc4UlWv8T0LLJENEFV0jYQXPIkkHWRVls1qGtRDzfBDkJOZVtXJr04TzY3jL9sIJnhlLUQeCID",
           "nonce": "OU5vTeMeNPAFUrr5",
           "timestamp": timestamp
           }
    list1 = sorted(url.items(), key=lambda item: item[0])
    list2 = []
    for i, j in list1:
        list2.append(str(i)+'='+str(j)+'&')
    str1 = str(''.join(list2))
    str2 = str1[:-1].encode('utf-8')
    sign = hashlib.sha1(str2).hexdigest()
    print(str2)
    print(sign)
    url_begin = 'https://clinicdemo.dxy.com/japi/open/500000?'
    request = requests.get(url_begin+str1+'doctor_id='+str(doctor_id)+'&sign='+sign)
    data = json.loads(request.text)
    response = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)

    print(response)


if __name__ == '__main__':
    test_500000()
