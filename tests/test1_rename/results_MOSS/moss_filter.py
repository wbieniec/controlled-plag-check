
# Importing the required modules 
import os
import statistics
import sys

from bs4 import BeautifulSoup

report_fname = 'index.html'
filtered_fname = 'moss_filtered.csv'
REQUIRED_PHRASE = "A.py"

  
# empty list
data = []
  
# for getting the header from
# the HTML file
list_header = []
soup = BeautifulSoup(open(report_fname),'html.parser')
header = soup.find_all("table")[0].find("tr")
 
for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue
 
# for getting the data 
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
 
for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)
 
print(data)
print()

filtered_data = []
for row in data:
  if any(REQUIRED_PHRASE in x for x in row):
    filtered_data.append([x.rstrip() for x in row])

filtered_data2 = []

for item in filtered_data:
  left, right, _ = item
  left_percent = float(left.split()[1][1:-2]) / 100
  right_percent = float(right.split()[1][1:-2]) / 100
  left_fname = left.split()[0].split("/")[-1]
  right_fname = right.split()[0].split("/")[-1]
  filtered_data2.append([left_fname, right_fname, str(statistics.geometric_mean([left_percent, right_percent])).replace(".",",")])
  

filtered_data2.sort(key = lambda x:x[1]) #Assume stable sort
filtered_data2.sort(key = lambda x:x[0])

with open(filtered_fname, "wt") as g:
  for row in filtered_data2:
    g.write(";".join(row) + "\n")
    
  
