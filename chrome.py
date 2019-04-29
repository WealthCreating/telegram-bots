import os
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')


class Chrome:
    def __init__(self):
        self._connect()

    def _connect(self):
        self.web = webdriver.Chrome(os.getcwd() + '/chromedriver', options=self.options)

    def refresh(self):
        self.web.close()
        self._connect()

    def get(url):
        self.web.get(url)
