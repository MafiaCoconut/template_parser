import requests
from requests.auth import HTTPBasicAuth
import json
import sqlite3
import os
import re
from bs4 import BeautifulSoup


def delete_tages_from_data(string):
    return ''.join(re.sub(r'(<p>|</p>)', "", string))


def get_data(url):
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.44 '
    }

    page = requests.get(url, headers=headers)
    with open('data/project.html', 'w', encoding='utf-8') as file:
        file.write(page.text)


def work_with_main_page(url):
    with open('data/project.html', encoding='utf-8') as file:
        page = BeautifulSoup(file.read(), 'lxml')
    print(page)

    # page = requests.get(url)
    # soup = BeautifulSoup(page.text, 'html.parser')
    #
    # airphones = soup.find_all('a', href=True, class_='model-short-title no-u')
    #
    # item = airphones[0]
    # name = item.text
    # url_item = 'https://www.e-katalog.ru' + item['href']
    # print(f"{name}, {url_item}")
    # item_page = requests.get(url_item)


def main():
    url = 'https://www.e-katalog.ru/ek-list.php?presets_=31131%2C2377%2C40978&katalog_=239&pf_=1&save_podbor_=1'

    # get_data(url)
    # from_site_to_lst(url)


if __name__ == '__main__':
    main()
