from bs4 import BeautifulSoup
from html.parser import HTMLParser


fin =  open("Turing Award - Wikipedia.html")
data = BeautifulSoup(fin, 'html.parser')
fin.close()

# print (data)
print (data.get_text())
full_table  = data.find('table', class_ = 'wikitable')
print (full_table)
# full_table = data.find_all("table")[1]
""" The find_all returns all the tables tag result set as a list: We
access the second list because previous year turing award Recipients is the second table in the htm page
"""

rows = full_table.find_all("tr") #and full_table.find_all("a")
"""
It gets the whole table values
"""

for row in rows:
	names = row.find_all("td")
	years = row.find_all("th")
	# values_scanned = row.find("a", {"title" : values.get_text()})
	# print (values_scanned)
	if years and years[0].get_text().strip().isnumeric():
		print ("\n" + years[0].get_text().strip())
	if names:
		name = names[0].get_text().strip()
		print (name)
	# print (rows[i].get_text())
	# print (rows[i])
	# if row.find("td"):
	# 	print (row.find("td").get_text())

# print (len(rows))
# for row in rows:
# 	print(row.get_text())

