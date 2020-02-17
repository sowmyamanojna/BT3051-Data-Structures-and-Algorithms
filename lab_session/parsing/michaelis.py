from bs4 import BeautifulSoup as bs

fin = open("michaelis.sbml")
data = bs(fin, 'lxml')
fin.close()

# print (data)

model = data.find('model')
# print (model)
val = model.listofspecies
ele = val.find_all('species')
for e in ele:
	# print (e['id'])
	# print (e['initialamount'])
	print (e)
	# e.sort()	
	# print (e)
ele.sort(['id'])