from bs4 import BeautifulSoup
import requests
from tagging import get_ner_results
from gsheet_util import update_results_to_gsheet
import io

def get_page_content(url):
    try:
        response = requests.get(url)
        print(response)

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all(['script', 'title'])
        page_text = ' '.join([para.get_text() for para in paragraphs])

        return page_text
    except Exception as e:
        print(e)
        return ''

if __name__ == '__main__':
    page_text = get_page_content('https://www.mbishop.com.tw/Article/Detail/79781')
    # with io.open('temp.txt', encoding='utf-8') as f:
    #     page_text = f.read()
    #     soup = BeautifulSoup(page_text, 'html.parser')
    #     paragraphs = soup.find_all(['script', 'title'])
    #     page_text = ' '.join([para.get_text() for para in paragraphs])

    results = get_ner_results(page_text)

    update_results_to_gsheet(results)