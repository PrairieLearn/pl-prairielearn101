import prairielearn as pl
import numpy as np
import networkx as nx
import random


def generate_dijkstra():
    
    while True:
    
        # some random weights
        n = np.random.randint(1,15, size=12)
    
        # un-comment this to test against https://www.prairielearn.org/pl/course_instance/129369/instructor/question/9073802/preview
        #n = np.array([2, 4, 7, 3, 3, 4, 3, 8, 6, 6, 8, 12])
        
        # create adjacency matrix, graph
        #              t     u     v     w     x     y     z
        adj=np.array([[0   , n[0], n[1], 0   , 0   , n[2], 0  ],  # t
                     [n[0], 0   , n[3], n[4], 0   , 0   , 0  ],  # u 
                     [n[1], n[3], 0   , n[5], n[6], n[7], 0  ],  # v
                     [0   , n[4], n[5], 0   , n[8], 0   , 0  ],  # w
                     [0   , 0   , n[6], n[8], 0   , n[9], n[10]],  # x
                     [n[2], 0   , n[7], 0   , n[9], 0   , n[11]],  # y
                     [0   , 0   , 0   , 0   , n[10], n[11], 0  ]]) # z
    
        G = nx.from_numpy_array(adj)
        labels = ['t', 'u', 'v', 'w', 'x', 'y', 'z']
        
        # select src
        src = random.choice(range(len(labels)))
        
        # this is a hacky way
        # to use random numbers, we must make sure there is a unique shortest path from src to each dest
        a, b = nx.dijkstra_predecessor_and_distance(G, src)
        # a is a list of predecessors of node, which will have one entry if there is a unique shortest path
        if max([len(val) for key, val in a.items()])==1:
            break
        # if we reach this point - there are multiple shortest paths, pick another graph
        
    return G, labels, src, n

def generate(data):
    
    # generate a problem instance
    G, labels, src, n = generate_dijkstra()

    # these are the costs and paths to each destination node
    l, path =  nx.single_source_dijkstra(G, src)

    # here is a list of dst, cost pairs sorted by cost, then dst index
    # we need this sort in order to generate the final path!
    l_srt = sorted(l.items(), key=lambda x: (x[1],x[0]), reverse=False)
    path_final = "".join([labels[entry[0]] for entry in l_srt])
    path_final_idx = [entry[0] for entry in l_srt]
    
    # these are the names of the destination nodes (not including the src)
    lr = labels[:src] + labels[src+1 :]
    # these are the indices of the destination nodes (not including the src)
    dst = [x for x in range(7) if x != src]
    
    # here are the distance for each of the destination nodes, in order of node index
    dist_final = [l[i] for i in dst]
    
    # here are the headers of the 
    d = {} # {'source': labels[src], 'col1': lr[0], 'col2': lr[1], 'col3': lr[2], 'col4': lr[3], 'col5': lr[4], 'col6': lr[5]}
    for i in range(7):

        # build a subgraph with the visited nodes, their neighbors, and edges that include at least one visited node
        
        nodes_subg_l = []
        for m in path_final_idx[:i+1]:
            nodes_subg_l.append(m)
            for neigh in G.neighbors(m):
                    nodes_subg_l.append(neigh)
        nodes_subg = np.unique(nodes_subg_l)
        edges_subg = []
        for e in G.edges(data=True):
            if e[0] in path_final_idx[:i+1] or e[1] in path_final_idx[:i+1]:
                edges_subg.append(e)
        subg=nx.Graph()
        subg.add_nodes_from(nodes_subg)
        subg.add_edges_from(edges_subg)
    
        # get predecessors and distances for this subgraph only
        pred, dist = nx.dijkstra_predecessor_and_distance(subg, src)
        

        d["path-%d" % i ] = path_final[:i+1]
        for j in range(1,7):
            column_node_index = dst[j-1]
            if column_node_index in dist:
                d["%d-%d" % (j,i) ] = "%d,%s" % (dist[column_node_index], labels[ min(pred[column_node_index])  ] ) 
            else:
                d["%d-%d" % (j,i) ] = 'inf'


    data['params'] = d
    data['correct_answers'] = d
    
    data['params']['source'] = labels[src]
    data['params']['lr'] = lr
    data['params']['n'] = n.tolist()
    data['params']['iter'] = [1, 2, 3, 4, 5, 6]
