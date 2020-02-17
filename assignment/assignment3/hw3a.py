# BT3051 Assignment 3a
# Roll number: BE17B007
# Collaborators: -
# Time: 10 mins

#Header information
import networkx as nx
import matplotlib.pyplot as plt


def RegularLattice(nodes, k):
	""" Function that creates and plots a reguar lattice"""
	#function body
	G = nx.Graph()
	for i in range(nodes):
		G.add_node(i)

	for i in range(nodes):
		for j in range(1, k+1):
			G.add_edge(i, (i+j)%nodes)
			G.add_edge(i, (i-j)%nodes)

	#statements to plot the lattice
	nx.draw_circular(G, with_labels=True)
	plt.show()

if __name__ == '__main__':
	
	RegularLattice(50,3)
