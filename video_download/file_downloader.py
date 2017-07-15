# _*_ coding: utf-8 _*_

"""
 by renjie
"""
import sys
import threading
from contextlib import closing

import requests

from video_download import constant


class FileDownloader(threading.Thread):
    def __init__(self, file_dir, chapter, id):
        threading.Thread.__init__(self)
        self.__file_dir = file_dir
        self.__chapter = chapter
        self.__id = id

    def run(self):
        url = self.__chapter.url
        fileName = self.__file_dir +"/"+ self.__chapter.name + ".mp4"
        print(url)
        with closing(requests.get(url, stream=True, timeout=10)) as response:
            constant.TOTAL += int(response.headers['content-length'])  # 内容体总大小
            with open(fileName, "wb") as file:
                for data in response.iter_content(chunk_size=constant.chunk_size):

                    file.write(data)
                    constant.LOCK.acquire()
                    self.refresh(count=len(data))
                    constant.LOCK.release()
    def refresh(self, count=1, status="正在下载"):
        constant.PERLIST[self.__id] += count
        now_count = 0
        for item in constant.PERLIST:
            now_count += item
        if now_count >= constant.TOTAL:
            status = "下载完成"
        #      【名称】状态 进度 单位 分割线 总数 单位
        # str = "【%s】%s %.2f %s %s %.2f %s" % ("项目", status, now_count / constant.chunk_size, "KB", "/", constant.TOTAL / constant.chunk_size, "KB")
        #      【名称】 状态 百分比
        str = "【%s】 %s %.2f%%" % ("视频文件", status, now_count * 100.0 / constant.TOTAL)
        sys.stdout.write(str + "\r")
        sys.stdout.flush()