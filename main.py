import requests
from requests.auth import HTTPBasicAuth
import json
import sqlite3
import os
import re
from bs4 import BeautifulSoup


def delete_tage_from_data(string):
    return ''.join(re.sub(r'(<p>|</p>)', "", string))


def get_data(url, headers, name):
    """
    name - название файла, котором вы хотите его назвать
    """
    page = requests.get(url, headers=headers)
    with open(f'data/{str(name)}.html', 'w', encoding='utf-8') as file:
        file.write(page.text)


def work_with_main_page(url, headers):
    # Открыть уже сохраннёный файл html         РЕКОМЕНДУЕТСЯ!!!
    with open('data/main_page.html', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')

    # Обратиться к сайту напрямую
    # page = requests.get(url, headers=headers)
    # soup = BeautifulSoup(page.text, 'lxml')

    print(soup)


def main():
    url = 'https://www.youtube.com/gaming/games'
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61 (Edition Yx GX 03)'
    }
    # get_data(url, headers, 'main_page')
    work_with_main_page(url, headers)


if __name__ == '__main__':
    main()
