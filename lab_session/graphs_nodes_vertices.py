class Vertex:

	def __init__(self, x):
		self._val = x

	def element(self):
		return self._val

	def __hash__(self):
		return hash(id(self))


class Edges:

	def __init__(self, o, d, x=None):
		self._ori = o
		self._des = d
		self._val = x

	def startpoint(self):
		return self._ori

	def endpoint(self):
		return self._des

	def opposite(self, u):
		if u == self._ori:
			return self._des
		else:
			return self._ori

	def element(self):
		return self._val

	def __hash__(self):
		return hash((self._ori, self._des))


class Graph:
	def __init__(self):
		self._vertices = {}

	def vertex_count(self):
		return len(self._vertices)

	def edge_count(self):
		return len(self._vertices.values())//2

	def vertices(self):
		return self._vertices.keys()

	def edges(self):
		edges = []
		data = self._vertices.values()
		for i in data:
			edges.append(data[i])

		return edges

	def get_edges(self, u, v):
		if u in self._vertices.keys():
			return self._vertices[u][v]
		else:
			return self._vertices[v][u]

	def degree(self, u):
		if u in self._vertices.keys():
			return len(self._vertices[u])
		else:
			return "Vertex not found"

	def incedent_edges(self, u):
		data = self._vertices.keys()
		if u in data:
			edges = []
			for i in data[u]:
				data.append(i.values())

		return 
