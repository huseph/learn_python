import urllib.request
import os

url1 = 'https://worldcosplay.net/member/Itsuki-chan/characters/'


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.3.314 Yowser/2.5 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

url = 'https://worldcosplay.net/photo/6859679'
print(url_open(url))

