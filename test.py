'''
* Download pics from https://worldcosplay.net/member/
* classify by characters
* made by Huseph
'''
import urllib.request
import os

url1 = 'https://worldcosplay.net/member/Itsuki-chan/characters/'


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.3.314 Yowser/2.5 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html
    


def get_page(url):
    html = url_open(url).decode('utf-8')
    
    pass#to be continued


def get_ch_name():
    pass
    


def character(ch_num, ch_name):
    os.mkdir(ch_name)
    os.chdir(ch_name)
    url_page = 'https://worldcosplay.net/api/member/126641/characters/' + str(ch_num) + '/photos.json?limit=16&p3_photo_list=true&page='
    for i in range(1,5)
        html += url_open(url_page + str(i))
    img_num1 = 0
    img_num1 = html.find('"id":', img_num1)
    while img_num1 != -1:
        img_num2 = html.find(',"url', img_num1)
        get_img(html[img_num1: img_num2])
        img_num1 = html.find('"id":', img_num1)
    
    
    url_ch = url + str(ch_num)

    page_url = url + '\' + 
    os.chdir('..')
    
def lets_roll():
    print('正在爬取图片...')
    
    os.mkdir('Itsuki-chan')
    os.chdir('Itsuki-chan')
    ch_num = 0
    html = url_open(url1)
    ch_num1= html.find('href="/member/Itsuki-chan/characters/', ch_num1) + 37
    while ch_num1 != -1:
        ch_num2= html.find('">', ch_num1)
        ch_name1 = html.find('<div class="photo_title">', ch_num1) + 25;
        ch_name2 = html.find('<', ch_name1)
        character(html[ch_num1: ch_num2], html[ch_name1: ch_name2])
        ch_num1 = html.find('href="/member/Itsuki-chan/characters/', ch_num1) + 37
    
        
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    lets_roll()
   