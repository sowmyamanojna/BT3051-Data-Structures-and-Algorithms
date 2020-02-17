import networkx as nx
import matplotlib.pyplot as plt

n = input("Enter number of nodes: ")
k = input("Enter number of k: ")

n = int(n)
k = int(k)

G = nx.Graph()
for i in range(n):
	G.add_node(i)

for i in range(n):
	for j in range(1,k+1):
		# print (i,(i+j+n)%n)
		G.add_edge(i,(i+j+n)%n)
		# print (i,(i-j+n)%n)
		G.add_edge(i,(i-j+n)%n)

nx.draw(G)
plt.show()