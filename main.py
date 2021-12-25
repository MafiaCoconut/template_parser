import requests
from requests.auth import HTTPBasicAuth
import json
import sqlite3
import os
import re
import time
from bs4 import BeautifulSoup
# from selenium import webdriver


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
    name = ''
    for i in range(len(lst)):

        if lst[i] == 'title':
            name = lst[i+4]

        if lst[i] == 'url':
            url_game = lst[i + 2]
            if 'channel' in url_game:
                count += 1
                urls.append(['https://www.youtube.com'+url_game+'/live', name])
                print(urls[-1])
                name = ''
                # print(url+url_game)
    print()
    req1 = requests.get(urls[0][0])
    print(req1.text)
    with open(f'data/{urls[0][1]}.html', 'w', encoding='utf-8') as file:
        file.write(req1.text)
    lst1 = req1.text.split('"')
    with open('data/test.html', 'w', encoding='utf-8') as file:
        file.write(str(lst1))




def main():
    # url = 'https://www.e-katalog.ru/ek-list.php?presets_=31131%2C2377%2C40978&katalog_=239&pf_=1&save_podbor_=1'
    url = 'https://www.youtube.com/gaming/games'
    headers = {
        'accept': 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61 (Edition Yx GX 03)'
    }
    # get_data(url, headers)
    work_with_main_page(url, headers)


if __name__ == '__main__':
    main()