import requests
import json
import csv

url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/13.886718/lat/57.76983/data.json"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.text


x = json.loads(data)

smhiData = []

for item in x["timeSeries"]:
    #print(type(item["parameters"]))
    for sPara in item["parameters"]:

        sDict = sPara
        
        sDict["values"] = sPara["values"][0]
        sDict["validTime"] = item["validTime"]
        sDict["geometryType"] = x["geometry"]["type"]
        sDict["geometryX"] = x["geometry"]["coordinates"][0][0]
        sDict["geometryY"] = x["geometry"]["coordinates"][0][1]
        sDict["approvedTime"] = x["approvedTime"]
        sDict["referenceTime"] = x["referenceTime"]
        #print(type(sDict))
        #print((sDict))
        smhiData.append(sDict)



with open('test.csv', 'w+', newline='') as csvfile:
   fieldnames = smhiData[0].keys()
   writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

   writer.writeheader()
   for dict in smhiData:
       writer.writerow(dict)  
