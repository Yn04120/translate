import requests
import os
import re
from bs4 import BeautifulSoup

def sticker(id):
    folder = 'line_image/' + str(id) + '/'
    if not os.path.exists(folder):
        os.makedirs(folder)

    url = f"https://store.line.me/stickershop/product/{id}/zh-Hant"
    html = requests.get(url)
    name = 1
    bs = BeautifulSoup(html.text, 'lxml')
    datas = bs.find_all('div', {'class': 'mdCMN09LiInner FnImage'})
    
    for e in datas:
        s = e.find('span')
        imgUrl =  'https:' + s['style'].split(':')[2][:-2]
        imgFile = requests.get(imgUrl)

        pattern = re.compile('[0-9]+')
        newindex = pattern.findall(imgUrl)[1]
        filename = folder + str(name) + '.png'
        with open(filename, 'wb') as f:
            f.write(imgFile.content)
        name +=1
