import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher"


def get_references_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    references = soup.find_all(class_="reference")
    return (f'\n The number of references is: {len(references)} \n')
#################################################################################################
def get_references_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    references = soup.find_all(class_="reference")
    list = 0
    for x in (references):
        list += 1
        print(f'{list}. references needed for report: \n {x.parent.text}')


print(get_references_needed_count(URL))
print(get_references_needed_report(URL))
