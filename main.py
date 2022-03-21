import os
import time
import requests
from lxml import etree
url = "https://www.huya.com/g/1663"
header = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
resp = requests.get(url,headers= header )
html = etree.HTML(resp.text)
image_list = html.xpath('//img[@class="pic"]')

path = './image/'
if not os.path.isdir(path):
    os.mkdir(path)

for image_date in image_list:
    image_url = image_date.xpath('./@data-original')[0]
    image_url = image_url.split('?')[0]
    image_name = image_date.xpath('./@alt')[0]
    image = requests.get(image_url)
    with open('./image/%s.jpg' % image_name ,'wb') as file:
        file.write(image.content )
    print('%s 下载完成。。。。' % image_name )
    time.sleep(1)