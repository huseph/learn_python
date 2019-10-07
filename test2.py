import urllib.request
import os

url1 = 'https://worldcosplay.net/member/Itsuki-chan/characters/'


def url_open(url):
    print('这是url::',url,'\n')
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.3.314 Yowser/2.5 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html
    



def get_img(img_num):
    url_aim = 'https://worldcosplay.net/photo/' + str(img_num)
    html = str(url_open(url_aim), encoding = 'utf-8')
    img_num1 = 0
    img_num1 = int(html.find('"image" src="', img_num1)) + 13
    img_num2 = int(html.find('"></div>\n\t\t\t</div>\n\t\t\t', img_num1))
  
    url_img = html[img_num1: img_num2]
    img = url_open(url_img)
    img_name = str(img_num) + '.jpg'
    with open(img_name, 'wb') as f:
        f.write(img)
  
get_img(6859679)