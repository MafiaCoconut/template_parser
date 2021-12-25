import requests
from requests.auth import HTTPBasicAuth
import json
import sqlite3
import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver


def delete_tages_from_data(string):
    return ''.join(re.sub(r'(<p>|</p>)', "", string))


def get_data(url, headers):
    # page = requests.get(url, headers=headers)
    driver = webdriver.Firefox()
    driver.get(url)
    with open('data/project.html', 'w', encoding='utf-8') as file:
        # file.write(page.text)
        file.write(driver.page_source)


def work_with_main_page(url, headers):
    with open('data/project.html', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')

    scripts = soup.find_all('a', class_="ScCoreLink-sc-udwpw5-0 fPdslK tw-link")
    urls = {}
    for i in scripts:
        half = i.get('href')
        h_key = half[half.rfind('/') + 1:].replace('%20', ' ')
        urls[h_key] = 'https://www.twitch.tv' + half
    list_g = urls.keys()
    print('list_g')
    # game = urls

    # items = scripts[13]
    # x = items.text
    # lst = x.split('"')
    # # print(lst)
    #
    # urls = []
    # count = 0
    # for i in range(len(lst)):
    #     if lst[i] == 'url':
    #         url_game = lst[i + 2]
    #         if 'channel' in url_game:
    #             count += 1
    #             # urls.append('youtube.com/channel'+url_game+'/live')
    #             urls.append(url+url_game+'/live')
    #             # print(url+url_game)
    # # for i in range(len(urls)):
    #
    #
    # print(urls[0])
    # game = requests.get(urls[0], headers=headers)
    # with open('data/GTA.html', 'w', encoding='utf-8') as file:
    #     file.write(game.text)
    # game_soup = BeautifulSoup(game.text, 'lxml')
    # print(game_soup)
    # game_page = game_soup.find_all('a', id='video-title')
    # print(game_page)
    # for j in game_page:
    #     print(j.text)


def main():
    # url = 'https://www.e-katalog.ru/ek-list.php?presets_=31131%2C2377%2C40978&katalog_=239&pf_=1&save_podbor_=1'
    url = 'https://www.twitch.tv/search?term=%D0%B8%D0%B3%D1%80%D1%8B&type=categories'
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61 (Edition Yx GX 03)'
    }
    # get_data(url, headers)
    work_with_main_page(url, headers)


if __name__ == '__main__':
    main()
