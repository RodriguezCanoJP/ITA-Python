import requests
import csv
import json


response = requests.get("https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=lUgmzFgrUwNniZUP5adSLNTDIn2gAfst")
info = response.json()
results = info['results']

keys = [key for key in results[0].keys()]

with open("output.csv", "w") as file:
    csv_file = csv.writer(file, dialect='excel')
    csv_file.writerow(keys)
    for item in results:
        csv_file.writerow([item[keys[0]], item[keys[1]], item[keys[2]], item[keys[3]], item[keys[4]], item[keys[5]], item[keys[6]], item[keys[7]], item[keys[8]], item[keys[9]], item[keys[10]]])

