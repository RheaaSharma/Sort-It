import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

df = pd.read_csv('app_info.csv')

names = df['track_name']
ids = df['id']
with open('apps.csv', mode='w') as apps:
    fieldnames = ['id', 'name', 'keywords']
    writer = csv.DictWriter(apps, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(0, names.size):
        name = names[i]
        URL = "https://apps.apple.com/us/app/" + name.replace(' ', '-') + "/id" + str(ids[i])
        print(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("meta", attrs={'name':'keywords'})
        if results is not None:
            try:
                writer.writerow({'id': ids[i], 'name': names[i], 'keywords': results.prettify()})
            except Exception:
                pass


