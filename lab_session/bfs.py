import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
# for i in range(5):
#     G.add_node(i)

# for i in range(5):
#     G.add_edge(i, (i+1)%5)
    
# for i in range(5, 8):
#     G.add_node(i)
    
# G.add_edge(5,6)
# G.add_edge(6,7)
# G.add_edge(5,4)
# G.add_edge(2,4)

# G.remove_edge(0,4)

for i in ['a','b','c','d','e','f','g']:
    G.add_node(i)

G.add_edges_from([('a','b'), ('a','c'), ('a','d'), ('c','d'), ('b','e'), ('e','f'), ('f','g'), ('c','f'), ('d','g')])

nx.draw(G, with_labels=True)
plt.show()

todolist = ['a']
visited = []

while todolist:
    i = todolist[0]
    for j in list(G.neighbors(i)):
        if (j not in todolist) and (j not in visited): todolist.append(j)
    todolist.remove(i)
    visited.append(i)
    
    print('todolist', todolist)
    print('visited', visited)
