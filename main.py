import requests
from requests.auth import HTTPBasicAuth
import json
import sqlite3
from bs4 import BeautifulSoup

"""
class="product_item product_item--promoted fast-sell-super" - класс одного автоа
url = https://youla.ru/moskva/auto
url2 = https://youla.ru/moskva/auto/s-probegom/vaz-lada-priora-2011-61bf298eff64e321931acafa


"""


def from_site_to_lst():
    url = 'https://www.e-katalog.ru/ek-list.php?presets_=31131%2C2377%2C40978&katalog_=239&pf_=1&save_podbor_=1'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup)
    airphones = soup.find_all('a', href=True, class_='model-short-title no-u')
    # print(airphones)
    # for item in airphones:
    item = airphones[0]
    name = item.text
    url_item = 'https://www.e-katalog.ru' + item['href']
    print(f"{name}, {url_item}")
    item_page = requests.get(url_item)



def main():
    from_site_to_lst()


if __name__ == '__main__':
    main()
