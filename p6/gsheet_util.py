import pygsheets
import pandas as pd

def update_results_to_gsheet(results):
    gc = pygsheets.authorize(service_file='../secret.json')

    df = pd.DataFrame(columns=['word', 'entity', 'score'])

    for i, result in enumerate(results):
        df.loc[i] = list(result)

    sh = gc.open('NER-tagging')

    wks = sh[0]  

    wks.set_dataframe(df,(0,0), encoding='utf-8')
