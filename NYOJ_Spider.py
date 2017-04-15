# A NYOJ data spider
# href: http://acm.nyist.net/JudgeOnline/problemset.php
# Code by Aston5128
# Only take 0.1s

from Download import dl
from bs4 import BeautifulSoup
import time
import threading


class nyoj:
    def __init__(self, filename):
        """Script start at here"""
        self.start_url = 'http://acm.nyist.net/JudgeOnline/profile.php?userid=Leida_'
        # Use gb18030 code
        input_file = open(filename, 'r', encoding='gb18030')
        # Listing names
        name_list_n = input_file.readlines()
        # take off the '\n' in the name value
        self.name_list = [name.replace('\n', '') for name in name_list_n]
        self.output_file = open('output_file.txt', 'w')
        # output to file with localtime
        self.output_file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n')

    def getAc(self, url, name):
        html = dl.GetHtml(url)
        ac_num = BeautifulSoup(html, 'lxml').find('table', class_='side-table').find_all('td')[3].text
        ac = name + ' ' + str(ac_num)
        print(ac)
        self.output_file.write(ac + '\n')

    def get(self):
        """Main def"""
        for name in self.name_list:
            url = self.start_url + name
            th = threading.Thread(target=self.getAc, args=(url, name))
            th.start()


if __name__ == '__main__':
    nyoj('input_file.txt').get()
