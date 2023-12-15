from bs4 import BeautifulSoup

import requests,openpyxl

excel=openpyxl.Workbook()
#print(excel.sheetnames)
sheet=excel.active
sheet.title='garden lab lab'
#print(excel.sheetnames)
sheet.append(['title','description'])


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

source = requests.get('https://vikaspedia.in/agriculture/crop-production/package-of-practices/pulses/garden-lab-lab', headers=headers,verify=False)

soup = BeautifulSoup(source.text, 'html.parser')

res = soup.find('div', id_="MiddleColumn_internal").find_all('li')

for i in res:
    name = i.find('h3', class_="ipc-title__text").text
    rank = i.find('h3', class_="ipc-title__text").get_text(strip=True).split('.')[0]
    year = i.find('span', class_="sc-4dcdad14-8 cvucyi cli-title-metadata-item").text
    rating = i.find('span', class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text.split()[0]
    print( rank,name, year, rating)
sheet.append([rank,name,year,rating])
excel.save('TOP IMDB Movie Ratings.xlsx')
