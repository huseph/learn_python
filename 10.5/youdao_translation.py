import urllib.request
import urllib.parse
import json
import time

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

data = {}

#data['i'] = 'Trim Trailing Space and Save'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15702467334151'
data['sign'] = '51f30c6edc8c07c2029eff506f0ff9c9'
data['ts'] = '1570246733415'
data['bv'] = '26d648eed529baef147bb9ef08c24259'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'


head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.3.314 Yowser/2.5 Safari/537.36'

while True:
    content = input('请输入需要翻译的内容(输入“!p”退出):\n')
    if content == '!p':
        break
    
    data['i'] = content
    data1 = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data1, head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    print(target['translateResult'][0][0]['tgt'])
    time.sleep(5)
    
