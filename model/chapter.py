# _*_ coding: utf-8 _*_

"""
 by renjie
"""

'''
章节
'''
class Chapter(object):
    def __init__(self):
        self.__name = ''
        self.__time = ''
        self.__url = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value