import datetime
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def collect_data(navarea_num:int = '4')->str:
    print('start downloading data from sealagom.com')

    #https://sealagom.com/navarea/4/
    url_base = 'https://sealagom.com'
    url_source = f'{url_base}/navarea/{navarea_num}/'
    print(url_source)

    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    ua = UserAgent()
    headers = {
        'User-Agent' : ua.random,
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
    }

    file_name = f'.\\downloads\\{navarea_num:02}_index_{navarea_num}.html'
    response = requests.get(url_source, headers = headers)

    soup = BeautifulSoup(response.text, 'lxml')
    navarea_text = soup.find('div', class_='message-content formatted' ).text.strip()

    file_name = f'.\\downloads\\{navarea_num:02}_Navarea_{navarea_num:02}.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(navarea_text)

    return navarea_text


def collect_data_tmp(navarea_num:int)->str:
    print('load tmp local files !!!')
    file_name = f'.\\downloads\\{navarea_num:02}_index_{navarea_num:02}.txt'
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
    return text