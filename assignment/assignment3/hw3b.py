# Header Information
# BT3051 Assignment 3b
# Roll number: BE17B007
# Collaborators: -
# Time: 0.5 days

def maze(MazeMatrix,start,finish):
	#MazeMatrix is a binary matrix (2D list of lists)
	#start & finish are tuples containing the starting and finishing point indices e.g. (1,1) & (5,5)
	
	#import statements, function body
	import networkx as nx
	# import matplotlib.pyplot as plt
	
	def MazeMatrix2Graph(MazeMatrix):
		#MazeMatrix is a binary matrix (2D list of lists)
		#function body
		nodes = {}
		vertices = []
		MazeGraph = nx.Graph()
		
		rows = len(MazeMatrix)
		if rows != 0: cols = len(MazeMatrix[0])
		
		for i in range(rows):
			for j in range(cols):
				if MazeMatrix[i][j] == 1:
					MazeGraph.add_node((i,j))
					
					if (i+1 < rows) and MazeMatrix[i+1][j]==1:
							MazeGraph.add_edge((i,j),(i+1,j))
					if (j+1 < cols) and MazeMatrix[i][j+1]==1:
							MazeGraph.add_edge((i,j),(i,j+1))
					if (i-1 >= 0) and MazeMatrix[i-1][j]==1:
						MazeGraph.add_edge((i,j),(i-1,j))
					if (j-1 >= 0) and MazeMatrix[i][j-1]==1:
							MazeGraph.add_edge((i,j),(i,j-1))
		
        # nx.draw(MazeGraph, with_labels=True)
		return MazeGraph #a networkx graph whose nodes represent the '1's in the input matrix. node labels are tuples.
	
	def MazeAnswerBFS(MazeGraph,start,finish):
		#MazeGraph is a networkx graph 
		#start and finish are tuples containing the starting and finishing point indices

		#function body 
		components = MazeComponentsDFS(MazeGraph)

		tree = None

		for i in components:
			if start and finish in i: tree = i

		if tree == None:
			return []

		path = {}
		for i in tree:
			path[i] = []

		todolist = [start]
		visited = []
		while todolist:
			n = todolist[0]
			for i in MazeGraph.neighbors(n):
				if (i not in todolist) and (i not in visited): 
					todolist.append(i)
					path[i] = path[n] + [n]
					if i == finish:
						path[i] += [i]
						break                    
			todolist.remove(n)
			visited.append(n)

		shortest_path = path[finish]

		return shortest_path #list of tuples containing indices of the points in the answer
	
	def MazeComponentsDFS(MazeGraph):
		#MazeGraph is a networkx graph
		
		#function body  
		lst = []
		nodes = nx.nodes(MazeGraph)
		components = []
		for i in nodes:
			if i not in lst:
				ccomp = []
				todolist = [i]
				visited = []
				while todolist:
					n = todolist[0]
					for j in MazeGraph.neighbors(n):
						if (j not in todolist) and (j not in visited): 
							todolist.insert(0, j)
					visited.append(n)
					todolist.remove(n)
					lst.append(n)
				ccomp.extend(visited)
			if ccomp not in components: 
				components.append(ccomp)

		return components #list of lists, each containing tuples of the indices of points in that component
	
	#function body
	MazeGraph = MazeMatrix2Graph(MazeMatrix)
	a = MazeAnswerBFS(MazeGraph, start, finish)
	b = MazeComponentsDFS(MazeGraph)
	print(a)
	print('\n')
	print(b)
#   a is the output of MazeAnswerBFS and b is the output of MazeComponentsDFS

if __name__ == '__main__':
	#DO NOT MODIFY THE FOLLOWING
	hw3bmaze=    [[1,0,1,1,0,1],
				  [1,1,0,0,0,0],
				  [0,1,0,1,1,1],
				  [0,1,1,1,0,1],
				  [1,0,0,1,1,1],
				  [1,1,0,0,0,1],
				  [0,0,1,1,0,1]]
	
	hw3bstart=(0,0)
	hw3bfinish=(6,5)
	maze(hw3bmaze,hw3bstart,hw3bfinish)

	
#output for this example should be:
#[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5)]
#[[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5), (3, 5), (2, 5), (2, 4), (2, 3)], [(0, 2), (0, 3)], [(0, 5)], [(4, 0), (5, 0), (5, 1)], [(6, 2), (6, 3)]]
