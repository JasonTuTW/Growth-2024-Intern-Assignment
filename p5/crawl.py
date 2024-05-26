import requests
import json
import config

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

def get_parse_results(items):
    parsed_results = []
    for item in items:
        result = {
            'title': item.get('title'),
            'snippet': item.get('snippet'),
            'link': item.get('link')
        }
        parsed_results.append(result)
    return parsed_results