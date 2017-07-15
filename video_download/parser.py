# _*_ coding: utf-8 _*_

"""
 by renjie
"""
from bs4 import BeautifulSoup

from video_download import constant
from video_download.model.chapter import Chapter


class iMoocParser(object):
    DOWNLOAD_URL = 'http://www.imooc.com/course/ajaxmediainfo/?mid={}&mode=flash'  # 下载链接
    def parser(self, course, fetcher, html):

        if html is None:
            return

        soup = BeautifulSoup(html, "lxml")
        course.name = soup.find('div', attrs={'class': 'hd clearfix'}).getText().strip()
        links = soup.find_all('a',class_='J-media-item')
        chapters = course.chapters
        for link in links:
            chapter = Chapter()
            type = link['href'].split('/')[1]
            if(type == "video"):#不是练习
                chapter.name = link.get_text().strip().replace(':','_').replace("\r\n","").replace(u'开始学习',"").replace(' ', '')
                id = link['href'].split('/')[2]
                json = fetcher.url_fetch(iMoocParser.DOWNLOAD_URL.replace('{}', id)).replace('\/', '/').encode('utf-8')
                dic_json = eval(json)
                # print dic_json['data']['result']['mpath'][0]
                # fileinfor.url['L'] = dic_json['data']['result']['mpath'][0]
                # fileinfor.url['M'] = dic_json['data']['result']['mpath'][1]
                chapter.url = dic_json['data']['result']['mpath'][constant.imooc_level]
                chapters.append(chapter)



class jikeParser(object):
    DOWNLOAD_URL = "http://www.jikexueyuan.com/course/video_download?seq=()&course_id={}"
    def parser(self, course, fetcher, html):
        if html is None:
            return
        soup = BeautifulSoup(html, "lxml")
        course.name = soup.find('div',attrs={'class':'bc-box'}).h2.getText().strip()
        links = soup.find_all('div', attrs={'class': 'text-box'})
        chapters = course.chapters
        url = jikeParser.DOWNLOAD_URL.replace("{}", course.id)
        seq = 1
        for link in links:
            chapter = Chapter()
            chapter.time = link.p.getText().strip()
            chapter.name = link.h2.a.getText().strip() + chapter.time.replace(":","_")
            json = fetcher.url_fetch(url.replace("()", str(seq))).replace('\/', '/').encode('utf-8')
            dic_json = eval(json)
            # print(dic_json['data']['urls'])
            chapter.url = dic_json['data']['urls']
            seq += 1

            chapters.append(chapter)

