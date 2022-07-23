from bs4 import BeautifulSoup
import requests

import json

URL = 'https://vincentarelbundock.github.io/Rdatasets/datasets.html'

def to_json(tag):
    
    return dict(
    {
        "Option": 
        {
            "Name": tag[1].text.strip(),
            "Title": tag[2].text.strip(),
            "Rows": tag[3].text.strip(),
            "Cols": tag[4].text.strip(),
            "Link": tag[10].a["href"]
        },
    })

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')

body = soup.find('tbody')

tr_tags = soup.find_all('tr')[2:]

js = {}
opt = [
]

with open("teste.json", "w") as f:
    for tr in tr_tags:
        td_tags = tr.find_all('td')
        opt.append(to_json(td_tags))
    js['Options'] = opt
    f.write(f'{json.dumps(js, indent=2)}\n')
