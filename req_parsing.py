import requests


class Parser:
    url = 'https://habr.com/ru/news/'
    domain = 'https://habr.com'

    def __init__(self):
        self.session: requests.Session = requests.Session()
        self.headers = {
            "User-Agent":'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
            "Accept":'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        }

    def parse(self, page=1) -> str:
        url = self.url + f"page{page}/"
        response = self.session.get(url)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f'{response.status_code} response code')
        return response.text

    def get_by_url(self, url) -> str:
        response = self.session.get(url)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f'{response.status_code} response code')
        return response.text

    @property
    def headers(self):
        pass

    @headers.setter
    def headers(self,value):
        self.session.headers = value

    @headers.getter
    def headers(self):
        return self.session.headers