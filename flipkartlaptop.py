from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

source=requests.get('https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace='
                    'FLIPKART&as-show=on&as=off')

source.raise_for_status()
soup=BeautifulSoup(source.text,'html.parser')
laptops=soup.find('div',class_='lister_list').find_all('div')
#print(len(laptops))

Name=[]
Price=[]
#Rating=[]



for laptop in soup.findAll('a',class_='_1fQZEK'):
      name=laptop.find('div',class_='_4rR01T').text.split('-')[0].strip()
      Name.append((name))
      price=laptop.find('div',class_='_30jeq3 _1_WHN1').text
      Price.append(price)
      #rating=laptop.find('div',class_='_3LWZlK').text.split(',')[0].strip()
      #Rating.append(rating)


'''
for laptop in soup.findAll('a',class_='_1fQZEK'):
      name=laptop.find('div',class_='_4rR01T')
      Name.append(name.text.split('-')[0].strip())
      price=laptop.find('div',class_='_30jeq3 _1_WHN1')
      Price.append(price.text)
      rating=laptop.find('div',class_='_3LWZlK')
      Rating.append(rating.text)
'''


d={'LAPTOP NAMES':Name,'PRICE':Price}
df=pd.DataFrame(d)
print(df)
df.to_csv('flipcartproduct.csv',index=None)


