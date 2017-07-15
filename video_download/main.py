# _*_ coding: utf-8 _*_

"""
 by renjie
"""
import os

from video_download.parser import iMoocParser, jikeParser

from video_download import constant
from video_download.fetcher import iMoocHost, iMoocFetcher, jikeHost, jikeFetcher
from video_download.file_downloader import FileDownloader
from video_download.model.course import Course


class SpiderGUI(object):

    def __init__(self):
        pass

    def crawl(self, url):
        # print(url.split('/')[-1].endswith("html"))
        course = Course()
        if iMoocHost in url:
            course_id = url.split("/")[-1]
            fetcher = iMoocFetcher()
            parser = iMoocParser()
        elif jikeHost in url:
            course_id = url.split("/")[-1].split(".")[0]
            fetcher = jikeFetcher()
            parser = jikeParser()
        course.id = course_id
        course.url = url
        html = fetcher.url_fetch(url)
        parser.parser(course, fetcher, html)
        return course

    def download(self, course, ids):

        file_dir = self.create_dir(course.name)
        print("下载到 %s" % file_dir)
        chapters = course.chapters
        if ids != '0':
            # print(ids.split(" "))
            chapters = [chapters[int(i) - 1] for i in ids.split(" ")]
        id = 0
        constant.PERSUM = len(chapters)
        for chapter in chapters:
            downloader = FileDownloader(file_dir, chapter, id)
            id += 1
            constant.PERLIST.append(0)
            downloader.start()


    def create_dir(self, course_name):
        path = course_name
        if len(constant.base_dir.strip()) != 0:
            path = constant.base_dir + "/" + course_name
        if os.path.exists(path) is not True:
            os.mkdir(path)
        return os.path.abspath(path)
    def show(self):
        print("#####################################################################")
        print("#慕课/极客学院 视频抓取器")
        print("author:包青蛙")
        print("慕课课程链接格式：http://www.imooc.com/learn/95")
        print("极客学院链接格式：http://www.jikexueyuan.com/course/3173.html")
        print("下载任务结束该程序会自动退出，需要同时下载的可以打开多个此程序")
        print("#####################################################################")
        try:
            url = input("输入要下载的课程链接：")
            # url = "http://www.jikexueyuan.com/course/3224.html"
            print("将要下载的课程链接为")
            print("开始解析视频")
            course = self.crawl(url)
            print("课程名： %s " % course.name)
            chapter_id = 1
            for chapter in course.chapters:
                print("-->%d. %s " % (chapter_id,chapter.name))
                chapter_id += 1
            ids = input("输入要下载的章节号（0则下载全部，多个用空格隔开)")
            self.download(course, ids)


        except Exception as X:
            raise TypeError('程序炸了') from X

if __name__ == '__main__':
    s = SpiderGUI()
    s.show()