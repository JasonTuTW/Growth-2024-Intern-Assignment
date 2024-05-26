import pygsheets
import pandas as pd

def update_results_to_gsheet(parsed_result, segmented_results):
    gc = pygsheets.authorize(service_file='../secret.json')

    df = pd.DataFrame(columns=['title', 'link', 'snippet', 'segmented_results'])

    for i, result in enumerate(parsed_result):
        df.loc[i] = [
            result['title'], 
            result['link'], 
            result['snippet'], 
            ' '.join(segmented_results[i])
        ]

    sh = gc.open('Web Crawl')

    wks = sh[0]  

    wks.set_dataframe(df,(0,0))
