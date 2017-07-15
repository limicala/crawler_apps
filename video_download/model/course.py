# _*_ coding: utf-8 _*_

"""
 by renjie
"""
'''
课程信息
'''
class Course(object):
    def __init__(self):
        self.__name = ''
        self.__id = ''
        self.__chapters = []
        self.__url = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def chapters(self):
        return self.__chapters

    @chapters.setter
    def chapters(self, value):
        self.__chapters = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value
