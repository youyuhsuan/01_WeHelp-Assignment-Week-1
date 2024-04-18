import urllib.request as req
import csv
from csv import DictReader
import json

url_1 = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1'
url_2 = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2'

stationname_list = []
attractiontitle_list = []

request_1 = req.Request(url_1)
with req.urlopen(request_1) as response:
    data_1 = response.read().decode('utf-8')
request_2 = req.Request(url_2)
with req.urlopen(request_2) as response:
    data_2 = response.read().decode('utf-8')

data_1 = json.loads(data_1)
data_2 = json.loads(data_2)

results_1 = data_1['data']['results']
results_2 = data_2['data']
  
with open('week3/task1/spot.csv',mode="w",encoding="utf-8") as file:
    
    for result_1 in results_1:
        SERIAL_NO_1 = result_1.get('SERIAL_NO', '')
        for result_2 in results_2:
            SERIAL_NO_2 = result_2.get('SERIAL_NO', '')
            if SERIAL_NO_1 == SERIAL_NO_2:
                address = result_2.get('address', '')
                district = address[5:8]         
                spottitle = result_1.get('stitle', '')
                longitude = result_1.get('longitude', '')
                latitude = result_1.get('latitude', '')
                filelist = result_1.get('filelist', '')
                links = filelist.split("https://")
                imageURL = "https://" + links[1]
                
                file.write("{},{},{},{},{}\n".format(spottitle, district, longitude, latitude, imageURL))

attractions_dict = {} 
for result_2 in results_2:
    stationname_2 = result_2.get('MRT', '')
    attractions_dict[stationname_2] = []
    
    for result_1 in results_1:
        stationname_1 = result_1.get('info', '')

        if stationname_2 in stationname_1:
            attractiontitle_list.append(result_1.get('stitle', ''))
            attractions_dict[stationname_2].append(result_1.get('stitle', ''))

with open('week3/task1/mrt.csv', mode="w",encoding="utf-8") as file:
    for station, attractions in attractions_dict.items():
        attractions_str = ",".join(attractions)  
        file.write("{},{}\n".format(station, attractions_str))