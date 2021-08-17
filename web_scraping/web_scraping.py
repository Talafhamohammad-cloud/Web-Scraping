import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"


def get_citations_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
