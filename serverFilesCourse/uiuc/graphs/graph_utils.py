import networkx as nx
import matplotlib.pyplot as plt
import random
from itertools import permutations, combinations, chain, product
from typing import List, Set, Tuple, Iterable, Union, DefaultDict, Optional, Callable, TypeVar
from collections import defaultdict
from random import sample, shuffle
from uiuc.shared_utils import grade_question_parameterized, QuestionData

TSPSolutionsDictT = DefaultDict[int, DefaultDict[int, int]]
VertexT = TypeVar('VertexT')

def generate_pl_graph(G: Union[nx.DiGraph, nx.Graph],
                      label: Optional[str] = None,
                      rankdir: str = "LR") -> str:
    """
    Generates a string usable by a pl-graph element.
    @param graph nx.DiGraph
        graph to construct string represenation of
    @return str
        representation of graph usable by a pl-graph element
    """
    visualize_graph = nx.nx_agraph.to_agraph(G)
    visualize_graph.graph_attr['rankdir'] = rankdir

    if label:
        for u,v in visualize_graph.edges():
            edge = visualize_graph.get_edge(u, v)
            edge.attr['label'] = edge.attr[label]

    return visualize_graph.to_string()

def get_weight_of_cycle(G: nx.DiGraph, cycle: List[int]) -> int:
    '''
    Finds weight of a cycle in graph.
    @param G nx.DiGraph
        graph to find weight of cycle in
    @param cycle list[int]
        list of ints representing nodes. The edges in the cycle are between each consecutive pair of nodes in the cycle,
        and there is an edge from the last node in the list to the first node in the list.
    @return int
        weight of cycle in graph
    @raises ValueError
        if cycle contains duplicate nodes or less than two nodes
    @raises KeyError
        if at least one of the following occurs:
        - an edge doesn't exist between a consecutive pair of nodes
        - there is no edge from the last node in the list to the first
        - a node in the list doesn't exist in the graph
    '''
    if len(set(cycle)) != len(cycle):
        raise ValueError('The cycle can only contain a node at most once.')
    if len(cycle) < 2:
        raise ValueError('The cycle must contain at least two nodes.')
    edges = set(G.edges())
    weight = 0

    for i in range(len(cycle)):
        next = (i + 1) % len(cycle)
        if (cycle[i], cycle[next]) in edges:
            weight += G[cycle[i]][cycle[next]]['weight']
        else:
            raise ValueError((
                f'Either the edge between node {cycle[i]} and node {cycle[next]} '
                f'does not exist, or at least one of these two nodes does not exist.')
            )

    return weight

def get_edge_count_of_shortest_negative_cycle(G: nx.DiGraph) -> Optional[int]:
    '''
    Finds edge count of shortest negative cycle.
    @param G nx.DiGraph
        graph to find shortest negative cycle in
    @return Optional[int]
        returns number of edges (int) in shortest negative cycle, if one exists
        returns None otherwise
    '''
    shortest_length = None
    for cycle in nx.algorithms.cycles.simple_cycles(G):
        if get_weight_of_cycle(G, cycle) < 0:
            if shortest_length is None:
                shortest_length = len(cycle)
            else:
                shortest_length = min(len(cycle), shortest_length)

    return shortest_length

def grade_toposort(data: QuestionData,
                   question_name: str,
                   vertices: Iterable[VertexT],
                   edges: Iterable[Tuple[VertexT, VertexT]],
                   transformation_function: Callable[[str], List[VertexT]]) -> None:
    '''
    Takes in data dictionary and checks if submission for topological ordering is correct.
    The submission is checked against the vertices and edges to check if it follows a valid topological ordering.
    transformation_function is used in order to handle multiple submission formats (comma separated list, just integers, etc).
    '''
    def grader(submission: str) -> Tuple[bool, str]:
        '''
        The grader function takes in the submission and sets it as correct/incorrect, with feedback messages.
        '''
        transformed_submission = transformation_function(submission)
        if not(set(transformed_submission) == set(vertices) and len(transformed_submission) == len(list(vertices))):
            return False, "Your input does not contain all vertices of the graph exactly once, or it contains vertices which are not in the graph."
        for (i, j) in edges:
            if transformed_submission.index(j) < transformed_submission.index(i):
                return False, f"The edge ({i},{j}) is not respected in your ordering."
        return True, "That's correct!"

    grade_question_parameterized(data, question_name, grader)

def traveling_salesman_dp_optimized_helper(G: nx.Graph) -> Tuple[int, TSPSolutionsDictT]:
    # Use the fact the nodes are the integers from 0,...,n
    start_vertex = 0
    lenG = len(G)

    notStart = list(G)
    notStart.remove(start_vertex)

    A = nx.to_scipy_sparse_array(G).todense().tolist()

    def subset_to_bitstring(s: Iterable) -> int:
        bs = 0
        for v in s:
            bs |= 1 << v
        return bs

    # visited vertices (starting from start_vertex) x last visited
    solutions: TSPSolutionsDictT = defaultdict(lambda: defaultdict(int))

    offsets = [~(1 << end) for end in range(lenG)]
    distances_from_start = A[start_vertex]

    for node in notStart:
        solutions[subset_to_bitstring([node])][node] = distances_from_start[node]

    for subs in chain.from_iterable(combinations(notStart, k) for k in range(2, lenG)):
        s_bs = subset_to_bitstring(subs)
        old_set_mem_arr = solutions[s_bs]

        for end in subs:
            new_set_mem_arr = solutions[s_bs & offsets[end]]
            distances = A[end]

            old_set_mem_arr[end] = min(
                new_set_mem_arr[end2] + distances[end2]
                for end2 in subs
                if end2 != end
            )

    solutions_dict = solutions[subset_to_bitstring(notStart)]

    return min(solutions_dict[node] + distances_from_start[node] for node in notStart), solutions

def traveling_salesman_dp_optimized(G: nx.Graph) -> int:
    total_weights, _ = traveling_salesman_dp_optimized_helper(G)
    return total_weights

def generate_tsp_test_case(num_nodes: int, weight_limit: int) -> nx.Graph:
    "Generate a complete graph with random weights"
    G = nx.complete_graph(num_nodes)

    for u, v in G.edges():
        G[u][v]['weight'] = random.randint(1, weight_limit)

    return G

def traveling_salesman_brute_force(G: nx.Graph, start_node: int = 0) -> Tuple[List[int], int]:
    "Computes the cheapest TSP tour by brute force"
    nodes = set(G.nodes)
    nodes.remove(start_node)

    cheapest_tour_weight = None
    cheapest_tour = None

    for tour_tuple in permutations(nodes):
        tour_weight = 0
        tour = [start_node] + list(tour_tuple) + [start_node]
        for u, v in zip(tour, tour[1:]):
            tour_weight += G[u][v]['weight']

        if cheapest_tour is None or cheapest_tour_weight > tour_weight:
            cheapest_tour = tour
            cheapest_tour_weight = tour_weight

    if cheapest_tour is None or cheapest_tour_weight is None:
        raise ValueError("Could not find cheapest tour")

    return cheapest_tour, cheapest_tour_weight


def generate_dag_with_hamiltonian_path(V: int, E: int) -> nx.DiGraph:
    """
    Generates a DAG with a Hamiltonian path
    """
    G = nx.DiGraph()
    vertices = list(range(V))

    G.add_nodes_from(vertices)

    shuffle(vertices)

    permutation_dict = {i: j for (i, j) in enumerate(vertices)}
    for i in range(V - 1):
        G.add_edge(permutation_dict[i], permutation_dict[i + 1])

    while len(G.edges) < E:
        u, v = sample(range(V), 2)

        min_vtx = min(u, v)
        max_vtx = max(u, v)

        G.add_edge(permutation_dict[min_vtx], permutation_dict[max_vtx])
    return G


def generate_dag_without_hamiltonian_path(V: int, E: int) -> nx.DiGraph:
    """
    Generates a DAG without a Hamiltonian path
    """
    G = nx.DiGraph()
    nodes_list = list(range(V))

    G.add_nodes_from(nodes_list)

    [src, sink, v1, v2] = sample(nodes_list, 4)

    # Remove source
    nodes_list.remove(src)
    nodes_list.remove(sink)

    # Add edes from source to every other vertex
    G.add_edges_from(product([src], nodes_list))

    # Add edges from every other vertex to sink
    G.add_edges_from(product(nodes_list, [sink]))

    while len(G.edges) < E:
        u, v = sample(nodes_list, 2)

        # Ensure no cycle
        if u in nx.descendants(G, v):
            continue

        G.add_edge(u, v)
        # Remove if Hamiltonian path created
        if v1 in nx.descendants(G, v2) or v2 in nx.descendants(G, v1):
            G.remove_edge(u, v)
    return G


def find_hamiltonian_path(G: nx.Graph) -> Optional[List]:
    """
    Returns a Hamiltonian path in G if it exists, None otherwise
    This is a complete search solution to the Hamiltonian path problem--runtime
    will be slow on large graphs.
    """
    if len(G) > 7:
        raise ValueError("Input graph is too large.")

    for potential_path in permutations(list(G)):
        edges = list(zip(potential_path, potential_path[1:]))
        if all(G.has_edge(first, second) for first, second in edges):
            return edges
    return None


def find_hamiltonian_cycle(G: nx.Graph) -> Optional[List]:
    """
    Returns a Hamiltonian cycle in G if it exists, None otherwise
    This is a complete search solution to the Hamiltonian cycle problem--runtime
    will be slow on large graphs.
    """
    if len(G) > 7:
        raise ValueError("Input graph is too large.")

    for potential_cycle in permutations(list(G)):
        edges = list(zip(potential_cycle, potential_cycle[1:])) + [(potential_cycle[0], potential_cycle[-1])]
        if all(G.has_edge(first, second) for first, second in edges):
            return edges
    return None


def draw_graph_counterexample(left_ax: plt.Figure, left_title: str, left_G: nx.Graph, left_highlight: Set,
                              right_ax: plt.Figure, right_title: str, right_G: nx.Graph, right_highlight: Set) -> None:

    left_ax.set_title(left_title, y = -0.1)
    right_ax.set_title(right_title, y = -0.1)

    left_edge_colors = ["red" if (u, v) in left_highlight or (
        v, u) in left_highlight else "black" for (u, v) in left_G.edges()]
    left_edge_widths = [3.0 if (u, v) in left_highlight or (
        v, u) in left_highlight else 1.0 for (u, v) in left_G.edges()]
    right_edge_colors = ["red" if (u, v) in right_highlight or (
        v, u) in right_highlight else "black" for (u, v) in right_G.edges()]
    right_edge_widths = [3.0 if (u, v) in right_highlight or (
        v, u) in right_highlight else 1.0 for (u, v) in right_G.edges()]

    nx.draw_circular(left_G, labels={n: n for n in left_G.nodes(
    )}, node_size=600, node_color="skyblue", edge_color=left_edge_colors, width=left_edge_widths, ax=left_ax)

    nx.draw_circular(right_G, labels={n: n for n in right_G.nodes(
    )}, node_size=600, node_color="sandybrown", edge_color=right_edge_colors, width=right_edge_widths, ax=right_ax)
