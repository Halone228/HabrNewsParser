import random
import time

from bs4 import BeautifulSoup
from req_parsing import Parser
from tqdm import tqdm

class Scrapper:
    page_num = 0
    def __init__(self):
        self.parser = Parser()

    def get_last_page(self) -> int:
        first_page = self.parser.parse()
        soup = BeautifulSoup(first_page, "lxml")
        last_page = soup.find('div', class_='tm-pagination__pages').find_all('a')[-1].text.strip()
        last_page = int(last_page)
        return last_page

    def scrape(self):
        last_page = self.get_last_page()
        end_arr = []
        for page in range(1,2):
            print('Parsing pages')
            raw_page = self.parser.parse(page)
            soup = BeautifulSoup(raw_page,"lxml")
            end_arr += list(self.scrape_pages(soup))
        return end_arr

    def scrape_pages(self,soup: BeautifulSoup):
        items_list = soup.find('div',class_='tm-articles-list')
        for _item in items_list.select('.tm-articles-list__item'):
            self.page_num += 1
            item = {'title':'','snippets':[],'description':'','url':'','img_src':'','raw_html':''}
            try:
                time.sleep(random.randrange(0,1))
                item = {
                    'title': _item.find('h2'),
                    'snippets':[item.text.strip() for item in _item.select('.tm-article-snippet__hubs-item')],
                    'description': _item.select_one('.article-formatted-body').text.strip(),
                    'url': self.parser.domain + _item.select_one('.tm-article-snippet__readmore').get('href')
                }
                try:
                    item['img_src'] = _item.select_one('.tm-article-snippet__lead-image').get('src')
                except:
                    pass
                item['raw_html'] = self.scrape_page(item['url'])
                yield item
            except Exception as e:
                print(e)
                print(item)

    def scrape_page(self,url) -> str:
        soup = BeautifulSoup(self.parser.get_by_url(url),"lxml")
        return str(soup.find('div',class_='tm-page__main'))