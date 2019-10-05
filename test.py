import urllib.request
import socket 
url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=IP&oq=%25E4%25BB%25A3%25E7%2590%2586IP&rsv_pq=c4a726160001b6ef&rsv_t=c3b53sQWCG7eHKNw3CROf9B1sYkbhmpsu5KMpG2bvZLtAFzTL4wFCiWq7Wk&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug2=0&inputT=264&rsv_sug4=264'

proxy_support = urllib.request.ProxyHandler({'http':'112.85.168.214:9999'})

opener = urllib.request.build_opener(proxy_support)

opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.3.314 Yowser/2.5 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)