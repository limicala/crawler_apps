# _*_ coding: utf-8 _*_

"""
 by renjie
"""
import logging
import requests
import constant
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"
iMoocHost = "www.imooc.com"
jikeHost = "www.jikexueyuan.com"

class iMoocFetcher(object):

    def __init__(self):
        self.session = requests.Session()
        self.clear_session()
        return

    def clear_session(self):
        self.session.headers.clear()
        self.session.cookies.clear()
        self.session.headers = {
            "User-Agent": USER_AGENT,
        }
        return

    def url_fetch(self, url):
        resp = self.session.get(url, allow_redirects=False, verify=False, timeout=5)
        if resp.status_code == 200:
            return resp.text
        logging.warning("Fetcher change cookie: %s", resp.status_code)
        self.clear_session()
        resp.raise_for_status()
        return resp.text



class jikeFetcher(object):
    COOKIE = "authcode=%s;uname=%s" % (constant.jike_authcode, constant.jike_uname)
    def __init__(self):
        self.session = requests.Session()
        self.clear_session()
        return

    def clear_session(self):
        self.session.headers.clear()
        self.session.cookies.clear()
        self.session.headers = {
            "User-Agent": USER_AGENT,
            "Cookie": jikeFetcher.COOKIE
        }
        # self.session.cookies = {
        #     "authcode": "533cXf3nwRK599f51%2FXb6oM0Ykui%2Fle8ILfQmUL1ptjhyVJR10ik85q31FrXWEAFK2kCIwgiNebZYMeh%2BYuET2OcXgVmeIm5DiJJnCkAr7Z%2F1XJZUK6luqqvN6AYQbj3",
        #     "uname": "jike_8429736",
        # }
        return

    def url_fetch(self, url):
        resp = self.session.get(url, allow_redirects=False, verify=False, timeout=5)
        if resp.status_code == 200:
            return resp.text
        logging.warning("Fetcher change cookie: %s", resp.status_code)
        self.clear_session()
        resp.raise_for_status()
        return resp.text