import numpy as np
import networkx as nx
import networkx.algorithms.isomorphism as iso
import itertools


# these are constants related to breadboard layout
bb_first_row = 111
bb_spacing = 18.62
bb_nrows = 30
bb_first_col_l = 194
bb_ncol_l = 5
bb_first_col_r = 326
bb_ncol_r = 5
bb_rows = np.array([bb_first_row + i*bb_spacing for i in range(bb_nrows)])
bb_cols = np.concatenate(([bb_first_col_l + i*bb_spacing for i in range(bb_ncol_l)], [bb_first_col_r + i*bb_spacing for i in range(bb_ncol_r)]))
bb_cols = np.append(bb_cols, [452.8, 471.76])
bb_cols = np.append([117.94, 136.88], bb_cols)

# these are constants related to element names in the graph
EL_RESISTOR    = 0  # resistor (both ends)
EL_LED_POS     = 1  # LED (anode)
EL_LED_NEG     = 2  # LED (cathode)
EL_VS_POS      = 3  # Voltage source (positive terminal)
EL_VS_NEG      = 4  # Voltage source (negative terminal)
EL_PUSH_BUTTON = 5  # Push button switch
EL_GPIO        = 6  # GPIO pin
EL_CAP_POS     = 7  # polarized capacitor positive terminal
EL_CAP_NEG     = 8  # polarized capacitor negative terminal
EL_CAP         = 9  # non-polarized capacitor terminal


LED_COLOR_VF   = {'red': 1.9, 'yellow': 2.1, 'green': 2.8, 'blue': 3.1, 'white': 3.1}
RES_INF        = int(1e12)
RES_VAR        = int(12345)
CAP_CER        = 0.1e-6
CAP_ELE        = 10e-6

# returns: row 1, row 2, column 1, column 2
def get_resistor_position(x):
    # for some reason if the part is placed but not moved, it's missing its width
    if 'width' not in x.keys():
        x['width']=60
    if 'height' not in x.keys():
        x['height']=16

    # note: resistors may be rotated
    y1 = x['top'] + np.sin( np.radians( x['angle'] ) )*x['width']/2.0 + np.cos( np.radians( x['angle'] ) )*x['height']/2.0
    y2 = x['top'] - np.sin( np.radians( x['angle'] ) )*x['width']/2.0 - np.cos( np.radians( x['angle'] ) )*x['height']/2.0
    x1 = x['left'] - np.cos( np.radians( x['angle'] ) )*x['width']/2.0 - np.sin( np.radians( x['angle'] ) )*x['height']/2.0
    x2 = x['left'] + np.cos( np.radians( x['angle'] ) )*x['width']/2.0 + np.sin( np.radians( x['angle'] ) )*x['height']/2.0

    return (np.abs(bb_rows - y1)).argmin(), (np.abs(bb_rows - y2)).argmin(), (np.abs(bb_cols - x2)).argmin(), (np.abs(bb_cols - x1)).argmin()


# returns: row 1, row 2, column 1, column 2 (1 is positive, 2 is negative terminal)
def get_led_position(x):
    # note: LEDs may not be rotated
    y1 = x['top'] + x['height']/2.0
    y2 = x['top'] + x['height']/2.0 - bb_spacing    
    x1 = x['left'] + x['width']/2.0 
    x2 = x['left'] - x['width']/2.0 

    return (np.abs(bb_rows - y1)).argmin(), (np.abs(bb_rows - y2)).argmin(), (np.abs(bb_cols - x2)).argmin(), (np.abs(bb_cols - x1)).argmin()


# returns: row 1, row 2, column 1, column 2 
def get_rvar_position(x):

    # note: variable resistors may not be rotated

    # light sensor is like resistor
    if x['rvartype']=="light":
    	y1 = x['top'] + np.sin( np.radians( x['angle'] ) )*x['width']/2.0 + np.cos( np.radians( x['angle'] ) )*x['height']/2.0
    	y2 = x['top'] - np.sin( np.radians( x['angle'] ) )*x['width']/2.0 - np.cos( np.radians( x['angle'] ) )*x['height']/2.0
    	x1 = x['left'] - np.cos( np.radians( x['angle'] ) )*x['width']/2.0 - np.sin( np.radians( x['angle'] ) )*x['height']/2.0
    	x2 = x['left'] + np.cos( np.radians( x['angle'] ) )*x['width']/2.0 + np.sin( np.radians( x['angle'] ) )*x['height']/2.0

    # temp sensor is like ceramic cap
    elif x['rvartype']=="temperature":
        y1 = x['top'] + x['height']/2.0
        y2 = x['top'] + x['height']/2.0
        x1 = x['left'] + x['width']/2.0
        x2 = x['left'] - x['width']/2.0

    return (np.abs(bb_rows - y1)).argmin(), (np.abs(bb_rows - y2)).argmin(), (np.abs(bb_cols - x2)).argmin(), (np.abs(bb_cols - x1)).argmin()

# returns: row 1, row 2, column 1, column 2 (if electrolytic, 1 is positive, 2 is negative terminal)
def get_capacitor_position(x):

    # note: caps may not be rotated

    # electrolytic has legs in two different rows
    if x['captype']=="electrolytic":
        y1 = x['top'] + x['height']/2.0
        y2 = x['top'] + x['height']/2.0 - bb_spacing
        x1 = x['left'] + x['width']/2.0
        x2 = x['left'] - x['width']/2.0

    # ceramic has legs in same row
    elif x['captype']=="ceramic":
        y1 = x['top'] + x['height']/2.0
        y2 = x['top'] + x['height']/2.0
        x1 = x['left'] + x['width']/2.0
        x2 = x['left'] - x['width']/2.0

    return (np.abs(bb_rows - y1)).argmin(), (np.abs(bb_rows - y2)).argmin(), (np.abs(bb_cols - x2)).argmin(), (np.abs(bb_cols - x1)).argmin()


# returns: row 1, row 2, column 1, column 2 
def get_push_button_position(x):

    # for some reason if the part is placed but not moved, it's missing its width
    if 'width' not in x.keys():
        x['width']=60
    if 'height' not in x.keys():
        x['height']=16

    if x['npins']==4:
        x1 = x['left'] - x['width']/2
        x2 = x['left'] + x['width']/2
        y1 = x['top'] - x['height']/2 + 4
        y2 = x['top'] + x['height']/2 - 4
    
        return (np.abs(bb_rows - y1)).argmin(), (np.abs(bb_rows - y2)).argmin(), (np.abs(bb_cols - x1)).argmin(), (np.abs(bb_cols - x2)).argmin()

    elif x['npins']==2:
        x1 = x['left'] - x['width']/2
        x2 = x['left'] + x['width']/2
        y1 = x['top'] - x['height']/2 + 4
        y2 = x['top'] + x['height']/2 - 4

        return (np.abs(bb_rows - y1)).argmin(), (np.abs(bb_rows - y2)).argmin(), (np.abs(bb_cols - x1)).argmin(), (np.abs(bb_cols - x2)).argmin()

# returns: row 1, row 2, column 1, column 2 
def get_wire_position(x):
    return (np.abs(bb_rows - x['y1'])).argmin(), (np.abs(bb_rows - x['y2'])).argmin(), (np.abs(bb_cols - x['x1'])).argmin(), (np.abs(bb_cols - x['x2'])).argmin()

# given row, column this returns the name of a breadboard terminal (side and row number; or power rail)
def get_term_from_row_col(row, col):
    if 2 <= col <= 11: # if we are in the "row" parts
        return ('L' if 2 <= col <= 6 else 'R')  +  str(row+1)
    else:        # if we are in the column parts
        if col==0:
            return 'L+'
        elif col==1:
            return 'L-'
        if col==12:
            return 'R+'
        elif col==13:
            return 'R-'
            

# pass the submitted elements and the dictionary of breadboard terminals and elements placed in them
# and the submission graph with initial elements added already
# return an updated bb_terms with the non-wire elements, and updated graph
def update_graph_from_components(placed, bb_terms, submission_graph):
    
    components_n = 0
    # update running count of components based on what's already in the bb_terms dictionary
    if len(bb_terms):
        components_n = max([max(v) for k,v in bb_terms.items()])
        
    for x in placed:
        
        if x['gradingName']=='pl-resistor':

            r_1, r_2, c_1, c_2 = get_resistor_position(x)

            key_1_terminal = get_term_from_row_col(r_1, c_1)
            key_2_terminal = get_term_from_row_col(r_2, c_2)

            if  key_1_terminal in bb_terms:
                bb_terms[key_1_terminal].append(components_n+1)
            else:
                bb_terms[key_1_terminal] = [components_n+1]

                
            if  key_2_terminal in bb_terms:
                bb_terms[key_2_terminal].append(components_n+2)
            else:
                bb_terms[key_2_terminal] = [components_n+2]

            # add to graph
            submission_graph.add_nodes_from( [(components_n+1, {"name": EL_RESISTOR  }), (components_n+2, {"name": EL_RESISTOR  }) ] )
            submission_graph.add_edge( components_n + 1, components_n + 2,  ohm=x['ohm'] )

            components_n += 2

        if x['gradingName']=='pl-rvar':

            r_1, r_2, c_1, c_2 = get_rvar_position(x)

            key_1_terminal = get_term_from_row_col(r_1, c_1)
            key_2_terminal = get_term_from_row_col(r_2, c_2)

            if  key_1_terminal in bb_terms:
                bb_terms[key_1_terminal].append(components_n+1)
            else:
                bb_terms[key_1_terminal] = [components_n+1]

                
            if  key_2_terminal in bb_terms:
                bb_terms[key_2_terminal].append(components_n+2)
            else:
                bb_terms[key_2_terminal] = [components_n+2]

            # add to graph
            submission_graph.add_nodes_from( [(components_n+1, {"name": EL_RESISTOR  }), (components_n+2, {"name": EL_RESISTOR  }) ] )
            submission_graph.add_edge( components_n + 1, components_n + 2,  ohm=RES_VAR )

            components_n += 2

        if x['gradingName']=='pl-capacitor':

            r_1, r_2, c_1, c_2 = get_capacitor_position(x)

            key_pos_terminal = get_term_from_row_col(r_1, c_1)
            key_neg_terminal = get_term_from_row_col(r_2, c_2)

            if  key_pos_terminal in bb_terms:
                bb_terms[key_pos_terminal].append(components_n+1)
            else:
                bb_terms[key_pos_terminal] = [components_n+1]

            if  key_neg_terminal in bb_terms:
                bb_terms[key_neg_terminal].append(components_n+2)
            else:
                bb_terms[key_neg_terminal] = [components_n+2]

            if x['captype']=="electrolytic":
                submission_graph.add_nodes_from( [(components_n+1, {"name": EL_CAP_POS  }), (components_n+2, {"name": EL_CAP_NEG  }) ] )
                submission_graph.add_edge( components_n + 1, components_n + 2, farad=CAP_ELE)
            elif x['captype']=="ceramic":
                submission_graph.add_nodes_from( [(components_n+1, {"name": EL_CAP  }), (components_n+2, {"name": EL_CAP  }) ] )
                submission_graph.add_edge( components_n + 1, components_n + 2, farad=CAP_CER )

            components_n += 2


        if x['gradingName']=='pl-led':
            
            r_1, r_2, c_1, c_2 = get_led_position(x)

            key_pos_terminal = get_term_from_row_col(r_1, c_1)
            key_neg_terminal = get_term_from_row_col(r_2, c_2)

            if  key_pos_terminal in bb_terms:
                bb_terms[key_pos_terminal].append(components_n+1)
            else:
                bb_terms[key_pos_terminal] = [components_n+1]
                
            if  key_neg_terminal in bb_terms:
                bb_terms[key_neg_terminal].append(components_n+2)
            else:
                bb_terms[key_neg_terminal] = [components_n+2]

            submission_graph.add_nodes_from( [(components_n+1, {"name": EL_LED_POS  }), (components_n+2, {"name": EL_LED_NEG  }) ] )
            submission_graph.add_edge( components_n + 1, components_n + 2, volt=LED_COLOR_VF[x['ledcolor']] )

            components_n += 2

        if x['gradingName']=='pl-push-button':

            r_1, r_2, c_1, c_2 = get_push_button_position(x)

            # 4-pin versions: two top pins connected internall, two bottom pins connected internally
            # between top and bottom (on either side), depends if switch is actuated
            if x['npins']==4:
                key_tl_terminal = get_term_from_row_col(r_1, c_1)
                key_bl_terminal = get_term_from_row_col(r_2, c_1)
                key_tr_terminal = get_term_from_row_col(r_1, c_2)
                key_br_terminal = get_term_from_row_col(r_2, c_2)

                if  key_tl_terminal in bb_terms:
                    bb_terms[key_tl_terminal].append(components_n+1)
                else:
                    bb_terms[key_tl_terminal] = [components_n+1]

                if  key_bl_terminal in bb_terms:
                    bb_terms[key_bl_terminal].append(components_n+2)
                else:
                    bb_terms[key_bl_terminal] = [components_n+2]

            elif x['npins']==2:
                key_1_terminal = get_term_from_row_col(r_1, c_1)
                key_2_terminal = get_term_from_row_col(r_2, c_2)

                if  key_1_terminal in bb_terms:
                    bb_terms[key_1_terminal].append(components_n+1)
                else:
                    bb_terms[key_1_terminal] = [components_n+1]

                if  key_2_terminal in bb_terms:
                    bb_terms[key_2_terminal].append(components_n+2)
                else:
                    bb_terms[key_2_terminal] = [components_n+2]

            # add to graph
            submission_graph.add_nodes_from( [(components_n+1, {"name": EL_PUSH_BUTTON  }), (components_n+2, {"name": EL_PUSH_BUTTON  }) ] )
            submission_graph.add_edge( components_n + 1, components_n + 2,  ohm=RES_INF )

            components_n += 2

    return bb_terms, submission_graph


# pass the dictionary of breadboard terminals and elements placed in them
# will return the connections between elements due to the breadboard strips
def get_bb_connections(bb_terms):
    connections = []
    for term_key in bb_terms:
        x = list(itertools.combinations(bb_terms[term_key], 2))
        for i in x:
            connections.append(i)
    return connections
    
    
# pass the submitted elements and the dictionary of breadboard terminals and elements placed in them
# always call this last, after all of the other components in bb_terms are complete
def get_wire_connections(placed, bb_terms):
    
    # first, map placed wires to breadboard terminals
    wires = []
    for w in placed:
        if w['gradingName']=='pl-line':
            r_1, r_2, c_1, c_2 = get_wire_position(w)
            wires.append( ( get_term_from_row_col(r_1, c_1) , get_term_from_row_col(r_2, c_2)) )
        # the 4-pin push button has internal connections that act like a wire
        # top left and top right connected internally
        # bottom left and bottom right connected internally
        elif w['gradingName']=='pl-push-button' and w['npins']==4: 
            r_1, r_2, c_1, c_2 = get_push_button_position(w)
            wires.append( ( get_term_from_row_col(r_1, c_1) , get_term_from_row_col(r_1, c_2)) )
            wires.append( ( get_term_from_row_col(r_2, c_1) , get_term_from_row_col(r_2, c_2)) )

    # now use that to construct a connectivity graph
    wire_graph = nx.Graph()
    wire_graph.add_nodes_from( list(sum(wires, ())) )
    wire_graph.add_edges_from( wires )

    connectivity = nx.all_pairs_node_connectivity(wire_graph)

    # from the connectivity graph, find out which pairs of terminals are connected by wires
    # (only terminals that have non-wire components in them - other terminals don't need to be part of the submission graph)
    wire_terms = {}
    for k1, v1 in connectivity.items():
        for k2, v2 in v1.items():
            if v2 and k1 in bb_terms and k2 in bb_terms:
                if k1 not in wire_terms:
                    wire_terms[k1] = []
                wire_terms[k1].extend(bb_terms[k1])
                wire_terms[k1].extend(bb_terms[k2])

    # finally, add connections between components in bb_terms based on wire_terms
    connections = []
    for term_key in wire_terms:
        x = list(itertools.combinations(wire_terms[term_key], 2))
        for i in x:
            if i[0]!=i[1]: # don't add self loops
                connections.append(i)
                
    return connections

def update_graph_add_connections(placed, bb_terms, submission_graph):

    connections = []

    # process all the connections due to the breadboard terminals
    bb_connections = get_bb_connections(bb_terms)
    connections.extend(bb_connections)
    
    # now, process all the wires
    wire_connections = get_wire_connections(placed, bb_terms)
    connections.extend(wire_connections)
    
    # add all of the connections between bb terms and from wires to the graph
    submission_graph.add_edges_from( connections )
    
    return submission_graph
