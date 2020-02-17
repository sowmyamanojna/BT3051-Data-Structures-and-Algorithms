from bs4 import BeautifulSoup
from html.parser import HTMLParser


fin =  open("Turing Award - Wikipedia.html")
data = BeautifulSoup(fin, 'html.parser')
fin.close()

print(data.prettify())