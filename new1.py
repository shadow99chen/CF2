# 第一种方式：requests 和 lxml结合使用

import requests

from lxml import etree

#1、拿到所有的页面链接，并使用yield返回完整的超链接

def get_html(url):

#     获取页面HTML

    html=requests.get(url)

#     使用etree格式化HTML

    seq=etree.HTML(html.text)

    link_list=seq.xpath('//*[@id="content"]/ul/li/a/@href')

    for i in link_list:

        yield "http://www.runoob.com"+i       

# 2、获取详细的页面数据

def get_html_link(link):

    for i in link:

#         获取界面

        link_html=requests.get(i)

#     初始化

        link_seq=etree.HTML(link_html.content)

#     得到标题

        title=link_seq.xpath('//*[@id="content"]/h1/text()')[0]

#     得到题目内容

        subject=link_seq.xpath('//*[@id="content"]/p[position()>1 and position()<4]/text()')

        subject_list='\n'.join(subject)

        yield (title,subject_list) 

# 3、保存数据

def save_subject(title_subject):

    with open("E:/SJSJ.txt",'a+',encoding='utf-8') as f:

        for title,subject_list in title_subject:

            f.write(title+'\n')

            f.write(subject_list+'\n')

            f.write("#"*50+'\n')

# 4、函数回调

def funcall(url):

    link=get_html(url)

    title_subject=get_html_link(link)

    save_subject(title_subject)

# 5、主函数

def main():

    url='http://www.runoob.com/python/python-100-examples.html'

    funcall(url)

if __name__=="__main__":

    main()

 

# for i in get_html('http://www.runoob.com/python/python-100-examples.html'):

#     print(i)

# for i in get_html_link(link):

#     print(i)
