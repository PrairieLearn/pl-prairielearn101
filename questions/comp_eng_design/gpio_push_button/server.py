import random, copy
import pl_breadboard as bb
import numpy as np
import networkx as nx
import networkx.algorithms.isomorphism as iso
import itertools


def generate(data):
    
    data['params']['pin'] = random.choice([17, 22, 27])
    data['params']['actuated'] = random.choice(['HIGH', 'LOW'])
    
    # first set up the solution graph and save it
    # this example has two possible solutions - either order of resistor vs LED is OK
    elements = [    (1, {"name": bb.EL_VS_POS}),
                    (2, {"name": bb.EL_VS_NEG}),
                    (3, {"name": bb.EL_RESISTOR}),
                    (4, {"name": bb.EL_RESISTOR}),
                    (5, {"name": bb.EL_PUSH_BUTTON}),
                    (6, {"name": bb.EL_PUSH_BUTTON}),
                    (7, {"name": bb.EL_RESISTOR}),
                    (8, {"name": bb.EL_RESISTOR}),
                    (9, {"name": bb.EL_GPIO, "pin": data['params']['pin'] }) ]
    attrs = {(3, 4): {"ohm": 220}, (7, 8): {"ohm": 10000}, (1, 2): {"volt": 3.3}, (5, 6): {"ohm": bb.RES_INF}}

    if data['params']['actuated']=="HIGH":
        # only solution: GPIO -- 220 resistor -- button
        #                V-   -- 10k resistor -- button
        #                button -- V+
        sol_graph_1 = nx.Graph()
        sol_graph_1.add_nodes_from( elements ) 
        sol_graph_1.add_edges_from( [(3, 4), (5,6), (7,8)] )
        nx.set_edge_attributes(sol_graph_1, attrs)
        sol_graph_1.add_edges_from( [ (9, 3), (4, 5), (6,1), (2,7), (8,5), (4,8) ])
    

        data['params']['solutions'] = [ nx.node_link_data(sol_graph_1)]
        
        data['params']['open'] = "LOW"
        data['params']['high-when-pressed'] = 'true'
        data['params']['low-when-pressed'] = 'false'

    elif data['params']['actuated']=="LOW":
        # only solution: GPIO -- 220 resistor -- button
        #                V+   -- 10k resistor -- button
        #                button -- V-
        sol_graph_1 = nx.Graph()
        sol_graph_1.add_nodes_from( elements ) 
        sol_graph_1.add_edges_from( [(3, 4), (5,6), (7,8)] )
        nx.set_edge_attributes(sol_graph_1, attrs)
        sol_graph_1.add_edges_from( [ (9, 3), (4, 5), (6,2), (1,7), (8,5), (4,8) ])
    
        data['params']['solutions'] = [ nx.node_link_data(sol_graph_1)]

        data['params']['open'] = "HIGH"
        data['params']['high-when-pressed'] = 'false'
        data['params']['low-when-pressed'] = 'true'

def grade(data):

    data['feedback']['breadboard'] = '<span class="badge badge-danger">0%</span>'
    data['feedback']['code'] = '<span class="badge badge-danger">0%</span>'
    
    # now set up the submission graph
    submission_graph = nx.Graph()
    
    # add voltage source and GPIO pin
    submission_graph.add_nodes_from( [(1, {"name": bb.EL_VS_POS  }), (2, {"name": bb.EL_VS_NEG  }), (9, {"name": bb.EL_GPIO, "pin": data['params']['pin'] }) ] )
    bb_terms = {'L+': [1], 'L-': [2], 'L12': [9]}

    # list of components placed by the user
    placed =  [d for d in data['submitted_answers']['bb'] if 'placed_by_user' in d.keys()]
    #for d in data['submitted_answers']['bb']:
    #    if 'placed_by_user' in d.keys():
    #        print(d['height'])

    # add the components to submission graph and to bb_terms dict
    bb_terms, submission_graph = bb.update_graph_from_components(placed, bb_terms, submission_graph)

    # process all the connections due to the breadboard terminals and wires
    submission_graph = bb.update_graph_add_connections(placed, bb_terms, submission_graph)

    # check if submission graph matches any of the solution graphs
    nm = iso.numerical_node_match(["name", "pin"], [-1, -1])
    em = iso.numerical_edge_match(["ohm", "volt"], [-1, -1])

    data['partial_scores']['bb']['score'] = 0
    #print(nx.node_link_data(submission_graph))
    for sol_graph in data['params']['solutions']:
        #print(sol_graph)
        if nx.is_isomorphic( nx.node_link_graph(sol_graph) , submission_graph, node_match = nm, edge_match = em):
            data['partial_scores']['bb']['score'] = 1
            data['feedback']['breadboard'] = '<span class="badge badge-success">100%</span>'


    if  data['partial_scores']['code']['score']==1:
        data['feedback']['code'] = '<span class="badge badge-success">100%</span>'
    elif data['partial_scores']['code']['score'] > 0:
        data['feedback']['code'] = '<span class="badge badge-warning">' + str(int(data['partial_scores']['code']['score']*100)) + '%</span>'
            
    data['score'] = 0.5*data['partial_scores']['bb']['score'] + 0.5*data['partial_scores']['code']['score']