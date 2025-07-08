import datetime
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def collect_data(navarea_num = '4'):
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

    file_name = f'index_{navarea_num}.html'
    response = requests.get(url_source, headers = headers)
    with open(file_name, 'w') as file:
         file.write(response.text)
    pprint(response.request.headers)

    with open(file_name, 'r') as file:
        src = file.read();

    soup = BeautifulSoup(src, 'lxml')
    navarea_text = soup.find('div', class_='message-content formatted' ).text.strip()
    print('',navarea_text, sep='\n')

    with open('1.txt', 'w') as file:
        print(navarea_text, file=file)


def plus(a,b):
    return  a+b


def main():
    for i in range(1,19):
        if(i == 13):
            continue
        collect_data(i)



if __name__ == '__main__':
    main()