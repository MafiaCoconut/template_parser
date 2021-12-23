import requests
from requests.auth import HTTPBasicAuth
import json
import sqlite3
import os
import re
from bs4 import BeautifulSoup


def delete_tages_from_data(string):
    return ''.join(re.sub(r'(<p>|</p>)', "", string))


def get_data(url, headers):
    page = requests.get(url, headers=headers)
    with open('data/project.html', 'w', encoding='utf-8') as file:
        file.write(page.text)


def work_with_main_page(url, headers):
    with open('data/project.html', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')
    # print(page)

    # page = requests.get(url, headers=headers)
    # soup = BeautifulSoup(page.text, 'lxml')

    scripts = soup.find('body').find_all('script')
    items = scripts[13]
    x = items.text
    lst = x.split('"')
    # print(lst)

    urls = []
    count = 0
    for i in range(len(lst)):
        if lst[i] == 'url':
            url_game = lst[i + 2]
            if 'channel' in url_game:
                count += 1
                urls.append(url+url_game)
                # print(url+url_game)






def main():
    # url = 'https://www.e-katalog.ru/ek-list.php?presets_=31131%2C2377%2C40978&katalog_=239&pf_=1&save_podbor_=1'
    url = 'https://www.youtube.com/gaming/games'
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61 (Edition Yx GX 03)'
    }
    # get_data(url, headers)
    work_with_main_page(url, headers)


if __name__ == '__main__':
    main()
