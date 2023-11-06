import requests
from bs4 import BeautifulSoup as BS
import csv
hackaton = requests.get('https://www.mashina.kg/search//?currency=2&price_from=&price_to=').text
hackaton1 = BS(hackaton, 'lxml')
hackaton2 = hackaton1.find_all('h2',class_='name')
hackaton7 = hackaton1.find_all('img', class_='lazy-image')


hackaton3 = hackaton1.find_all('strong')
for i in hackaton2:
    # print(i.text)
    for i2 in hackaton3:
        # print(i2.text)
        for i3 in hackaton7:
            # print(i.get('data-src'))
            dict_ = {
                    'title': i.text.strip(),
                  'price': i2.text ,
                  'img': i3.get('data-src') 
                }
            with open('csv_file.csv', 'a') as f:
                names = ['title', 'price', 'img']
                writer1 = csv.DictWriter(f, delimiter='|', fieldnames=names)
                writer1.writerow(dict_)
