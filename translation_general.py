import hashlib
# m = hashlib.md5()
# m.update(b'Nobody inspects')
# print(m.hexdigest())

words = 'good moring'

import requests
import random
import json
def translateBD(words,goallan):
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    q = words
    orginlan = 'auto'
    tolan = goallan
    appid = '20190414000287772'
    secretkey = '1yLfJfnxPrbWdqDhdtN0'
    salt = str(random.randint(32768,65535))
    sign = appid + q + salt +  secretkey
    m = hashlib.md5()
    m.update(sign.encode('utf8'))
    sign = m.hexdigest()
    d1 = {
        'q':q,
        'from':orginlan,
        'to':tolan,
        'appid':appid,
        'salt':salt,
        'sign':sign
    }
    r = requests.get(url,d1)
    result = json.loads(r.text)
    final_re =result['trans_result'][0]['dst']
    return final_re
