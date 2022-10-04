from email import header
import requests
from requests.auth import HTTPBasicAuth
import csv


def comparator(str1, str2):
    if str1.lower() > str2.lower():
        return 1
    elif str2.lower() > str1.lower():
        return 0
    else:
        return 0
    

response = requests.get("https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=kYfQWtOOA0NIY4OcSLtk5kiYos4htK5d")

print(response)
info = response.json()
results = info['results']
ordered_results = []
keys = [key for key in results[0].keys()]

for i in range(len(results)):
    for j in range(len(results)):
        if comparator(results[i]['title'], results[j]['title']) == 1:
            temp = results[j]
            results[j] = results[i]
            results[i] = temp
        else:
            continue


with open("output.csv", "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(keys)
    for item in results:
        csv_file.writerow([item[keys[0]], item[keys[1]], item[keys[2]], item[keys[3]], item[keys[4]], item[keys[5]], item[keys[6]], item[keys[7]], item[keys[8]], item[keys[9]], item[keys[10]]])

