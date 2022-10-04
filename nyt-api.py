import requests
import csv
import json


response = requests.get("https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=lUgmzFgrUwNniZUP5adSLNTDIn2gAfst")
info = response.json()
resultsInfo = info['results']
print(resultsInfo[2]['title'].lower())