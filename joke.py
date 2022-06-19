import requests
from bs4 import BeautifulSoup
import re

from random import choice
origin_url = 'https://xiaohua.zol.com.cn/yijuhua/' #冷笑话

def get_url_msg(origin_url):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/77.0.3865.120 Safari/537.36'}
    response = requests.get(origin_url, headers=head)  # 从链接中获取到回复信息
    bsobj = BeautifulSoup(response.text, 'lxml')    #利用bs解析
    return bsobj

bsobj = get_url_msg(origin_url)
link_list = []
for a_tag in bsobj.find_all('a', string = re.compile('查看全文')):
    link = a_tag.get('href')
    if link:
        link_list.append(link)
origin_url = origin_url.split('/')

words_list = []
for link in link_list:
    article_link = origin_url[0]+"//"+origin_url[2]+link
    bsobj = get_url_msg(article_link)

    for article_text in bsobj.find_all(name="div", attrs={"class" :"article-text"}):
        article = article_text.get_text()
        article = article.replace(" ","")
        #article = article.split()
        re.sub("[\n]+","",article)
        #print(article)
        words_list.append(article)

# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def text_create(name, msg):
    desktop_path = ""  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, "wb+")
    file.write(msg.encode("utf-8"))  # msg也就是下面的msg!
    file.close()

def joke():
    origin_url = 'https://xiaohua.zol.com.cn/yijuhua/'  # 冷笑话
    bsobj = get_url_msg(origin_url)
    link_list = []
    for a_tag in bsobj.find_all('a', string=re.compile('查看全文')):
        link = a_tag.get('href')
        if link:
            link_list.append(link)
    origin_url = origin_url.split('/')
    words_list = []
    for link in link_list:
        article_link = origin_url[0] + "//" + origin_url[2] + link
        bsobj = get_url_msg(article_link)

        for article_text in bsobj.find_all(name="div", attrs={"class": "article-text"}):
            article = article_text.get_text()
            article = article.replace(" ", "")
            # article = article.split()
            re.sub("[\n]+", "", article)
            # print(article)
            words_list.append(article)
    return choice(words_list)