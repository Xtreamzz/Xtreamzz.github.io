import requests
from bs4 import BeautifulSoup
import json

page = requests.get("https://republika.co.id/")
obj = BeautifulSoup(page.text,'html.parser');


print('\nMenampilkan title browser')
print('======================================')
print(obj.title.text)

#print('\nMenampilkan semua teks h2')
#print('======================================')
#for headline in obj.find_all('h2'):
#    print(headline.text)

print('\nMenampilkan headline berdasarkan div class')
print('=============================================')
for headline in obj.find_all('div',class_='conten1'):
    print (headline.find('h2').text)

print('\nMenampilkan kategori')
print('=============================================')
for publish in obj.find_all('div',class_='conten1'):
    print (publish.find('a').text)

print('\nMenampilkan waktu publish')
print('=============================================')
for publish in obj.find_all('div',class_='date'):
    print (publish.text)

print('\nMenampilkan waktu scrapping')
print('=============================================')
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time = ",current_time)

# Deklarasi list kosong
data=[]
# Lokasi file json
f=open('D:\scraping\headline.json','w')
for publish in obj.find_all('div',class_='conten1'):
    # append headline ke variable data
    data.append({'judul':publish.find('h2').text,'kategori':publish.find('a').text,'waktu_publish':publish.find('div',class_='date').text,'waktu_scraping':now.strftime("%Y-%m-%d %H:%M:%S")})
# dump list dictionary menjadi json
jdumps = json.dumps(data, indent=2)
f.writelines(jdumps)
f.close()
