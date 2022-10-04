import requests
import csv



def comparator(str1, str2):
    if str1[0].lower() > str2[0].lower():
        return 0
    elif str2[0].lower() > str1[0].lower():
        return 1
    else:
        return comparator(str1[1:], str2[1:])



response = requests.get("https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=lUgmzFgrUwNniZUP5adSLNTDIn2gAfst")
info = response.json()
results = info['results']

ordered_results = []
keys = [key for key in results[0].keys()]

for i in range(len(results)):
    for j in range(len(results)):
        lowest = " "
        if comparator(lowest, results[j]['title']) == 1:
            lowest = results[j]
        else:
            continue
    ordered_results.append(lowest)
    results.remove(lowest)




with open("output.csv", "w") as file:
    csv_file = csv.writer(file, dialect='excel')
    csv_file.writerow(keys)
    for item in ordered_results:
        csv_file.writerow([item[keys[0]], item[keys[1]], item[keys[2]], item[keys[3]], item[keys[4]], item[keys[5]], item[keys[6]], item[keys[7]], item[keys[8]], item[keys[9]], item[keys[10]]])

