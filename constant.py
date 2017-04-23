# _*_ coding: utf-8 _*_

"""
 by renjie
"""
import threading
from util import Properties
PERLIST=[]#记录每个线程的进度

LOCK = threading.Lock()#线程锁

PERSUM=0.0#用于描述总进度

TOTAL=0.0
dictProperties=Properties("config").getProperties()

chunk_size = int(dictProperties.get("chunk_size")) # 单次请求最大值

jike_authcode = dictProperties.get("jike_authcode")

jike_uname = dictProperties.get("jike_uname")

imooc_level = int(dictProperties.get("imooc_level")) #慕课视频的清晰度 0为普清，1为高清，2为超清

base_dir = str(dictProperties.get("base_dir"))