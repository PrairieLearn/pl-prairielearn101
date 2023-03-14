import random, copy
import pl_breadboard as bb
import numpy as np
import networkx as nx
import networkx.algorithms.isomorphism as iso
import itertools


def generate(data):
    
    data['params']['pin'] = random.choice([17, 22, 27])
    data['params']['active'] = random.choice(['HIGH', 'LOW'])
    
    # first set up the solution graph and save it
    # this example has two possible solutions - either order of resistor vs LED is OK
    elements = [    (1, {"name": bb.EL_VS_POS}),
                    (2, {"name": bb.EL_VS_NEG}),
                    (3, {"name": bb.EL_RESISTOR}),
                    (4, {"name": bb.EL_RESISTOR}),
                    (5, {"name": bb.EL_LED_POS}),
                    (6, {"name": bb.EL_LED_NEG}),
                    (7, {"name": bb.EL_GPIO, "pin": data['params']['pin'] }) ]
    attrs = {(3, 4): {"ohm": 220}, (1, 2): {"volt": 3.3}, (5, 6): {"volt": bb.LED_COLOR_VF['red']}}

    if data['params']['active']=="HIGH":
        # first solution: GPIO -- resistor -- LED -- V-
        sol_graph_1 = nx.Graph()
        sol_graph_1.add_nodes_from( elements ) 
        sol_graph_1.add_edges_from( [(3, 4), (5,6)] )
        nx.set_edge_attributes(sol_graph_1, attrs)
        sol_graph_1.add_edges_from( [ (7, 3), (4, 5), (6,2) ])
    
        # second solution: GPIO -- LED -- resistor -- V-
        sol_graph_2 = nx.Graph()
        sol_graph_2.add_nodes_from( elements ) 
        sol_graph_2.add_edges_from( [(3, 4), (5,6)] )
        nx.set_edge_attributes(sol_graph_2, attrs)
        sol_graph_2.add_edges_from( [ (7, 5), (6, 3), (4, 2) ])
    
        data['params']['solutions'] = [ nx.node_link_data(sol_graph_1), nx.node_link_data(sol_graph_2)]
        
        data['params']['opp'] = "LOW"

    elif data['params']['active']=="LOW":
        # first solution: V+ -- resistor -- LED -- GPIO
        sol_graph_1 = nx.Graph()
        sol_graph_1.add_nodes_from( elements ) 
        sol_graph_1.add_edges_from( [(3, 4), (5,6)] )
        nx.set_edge_attributes(sol_graph_1, attrs)
        sol_graph_1.add_edges_from( [ (1, 3), (4, 5), (6,7) ])
    
        # second solution: V+ -- LED -- resistor -- GPIO
        sol_graph_2 = nx.Graph()
        sol_graph_2.add_nodes_from( elements ) 
        sol_graph_2.add_edges_from( [(3, 4), (5,6)] )
        nx.set_edge_attributes(sol_graph_2, attrs)
        sol_graph_2.add_edges_from( [ (1, 5), (6, 3), (4, 7) ])
    
        data['params']['solutions'] = [ nx.node_link_data(sol_graph_1), nx.node_link_data(sol_graph_2)]

        data['params']['opp'] = "HIGH"

def grade(data):

    data['feedback']['breadboard'] = '<span class="badge badge-danger">0%</span>'
    data['feedback']['code'] = '<span class="badge badge-danger">0%</span>'
    
    # now set up the submission graph
    submission_graph = nx.Graph()
    
    # add voltage source and GPIO pin
    submission_graph.add_nodes_from( [(1, {"name": bb.EL_VS_POS  }), (2, {"name": bb.EL_VS_NEG  }), (7, {"name": bb.EL_GPIO, "pin": data['params']['pin'] }) ] )
    bb_terms = {'L+': [1], 'L-': [2], 'L12': [7]}

    # list of components placed by the user
    placed =  [d for d in data['submitted_answers']['bb'] if 'placed_by_user' in d.keys()]

    # add the components to submission graph and to bb_terms dict
    bb_terms, submission_graph = bb.update_graph_from_components(placed, bb_terms, submission_graph)

    # process all the connections due to the breadboard terminals and wires
    submission_graph = bb.update_graph_add_connections(placed, bb_terms, submission_graph)

    # check if submission graph matches any of the solution graphs
    nm = iso.numerical_node_match(["name", "pin"], [-1, -1])
    em = iso.numerical_edge_match(["ohm", "volt"], [-1, -1])

    data['partial_scores']['bb']['score'] = 0
    for sol_graph in data['params']['solutions']:
        if nx.is_isomorphic( nx.node_link_graph(sol_graph) , submission_graph, node_match = nm, edge_match = em):
            data['partial_scores']['bb']['score'] = 1
            data['feedback']['breadboard'] = '<span class="badge badge-success">100%</span>'


    if  data['partial_scores']['code']['score']==1:
        data['feedback']['code'] = '<span class="badge badge-success">100%</span>'
    elif data['partial_scores']['code']['score'] > 0:
        data['feedback']['code'] = '<span class="badge badge-warning">' + str(int(data['partial_scores']['code']['score']*100)) + '%</span>'
            
    data['score'] = 0.5*data['partial_scores']['bb']['score'] + 0.5*data['partial_scores']['code']['score']