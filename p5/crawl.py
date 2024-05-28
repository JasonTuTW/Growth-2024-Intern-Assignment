import requests
import json
import config
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from tqdm import tqdm

def google_search(query, start_index=1):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={config.API_KEY}&cx={config.SEARCH_ENGINE_ID}&start={start_index}"
    response = requests.get(url)
    return response.json()

def get_search_results(query, num_pages=3):
    results = []
    for page in range(num_pages):
        start_index = page * 10 + 1
        search_response = google_search(query, start_index)

        if 'items' in search_response:
            results.extend(search_response['items'])
        else:
            break
    return results

def get_page_content(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        response.html.render(sleep=3)
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        page_text = ' '.join([para.get_text() for para in paragraphs])

        return page_text
    except:
        return ''

def get_parse_results(items):
    parsed_results = []
    for item in tqdm(items):
        result = {
            'title': item.get('title'),
            'link': item.get('link')
        }
        result['content'] = get_page_content(result['link'])
        #print(result['content'])
        parsed_results.append(result)
    return parsed_results