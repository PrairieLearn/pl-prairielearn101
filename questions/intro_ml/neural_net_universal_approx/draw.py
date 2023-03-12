import networkx as nx
import matplotlib.pyplot as plt

inputLayerSize = 1
outputLayerSize = 1
hiddenLayerSize = 2

nodePos = {}
G=nx.Graph()
graphHeight = max(inputLayerSize, outputLayerSize, hiddenLayerSize)

# create nodes and note their positions
for n in range(inputLayerSize):
  nodePos['x'+str(n+1)]=(1, n)
  G.add_node('x'+str(n+1))
for n in range(outputLayerSize):
  nodePos['o'+str(n+1)]=(5, n)
  G.add_node('o'+str(n+1))
for n in range(hiddenLayerSize):
  nodePos['h'+str(n+1)]=(3, n)
  G.add_node('h'+str(n+1))

# add edges
for n in range(hiddenLayerSize):
  for m in range(inputLayerSize):
    G.add_edge('x' + str(m+1), 'h' + str(n+1))
  for m in range(outputLayerSize):
    G.add_edge('h' + str(n+1), 'o' + str(m+1))
nodePos['xb']=(1, inputLayerSize)
G.add_node('xb')
for n in range(hiddenLayerSize):
  G.add_edge('xb', 'h' + str(n+1))

nodePos['hb']=(3, hiddenLayerSize)
G.add_node('hb')
for n in range(outputLayerSize):
  G.add_edge('hb', 'o' + str(n+1))

plt.figure(figsize=(8, 6));
nx.draw_networkx(G, pos=nodePos, 
                 node_size=2000, node_color='pink')

#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,nodePos,edge_labels=labels)

edge_labels={
    ('x1', 'h1'): 'x1-h1', ('x1', 'h2'): 'x1-h2', 
    ('h1', 'o1'): 'h1-o1', ('h2', 'o1'): 'h2-o1', ('hb', 'o1'): 'hb-o1', ('xb', 'h1'): 'xb-h1', ('xb', 'h2'): 'xb-h2'
}


#nx.draw_networkx_edge_labels(G,nodePos,  edge_labels=edge_labels, 
#                          rotate=False, label_pos=0.22);


plt.margins(0.2, 0.2)

# Save the figure 
plt.savefig("network.png", format='png')


