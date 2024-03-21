from uiuc.graphs.graph_utils import draw_graph_counterexample, find_hamiltonian_cycle, find_hamiltonian_path
from uiuc.shared_utils import sized_powerset
from pl_helpers import name, points, save_plot
from pl_unit_test import PLTestCase
from code_feedback import Feedback

from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.insert(1, '/grade/serverFilesCourse')

class Test(PLTestCase):

    @points(10)
    @name('Check all possible graphs with four vertices')
    def test_0(self) -> None:
        n = 4

        for edge_set in sized_powerset(combinations(range(n), 2), min_size=1):
            g = nx.empty_graph(n)
            g.add_edges_from(edge_set)

            try:
                g_prime = self.st.f(g)

                cycle = find_hamiltonian_cycle(g)
                path = find_hamiltonian_path(g_prime)
                if bool(cycle) != bool(path):
                    left_ax, right_ax = plt.figure().subplots(1, 2)

                    left_edges = set() if cycle is None else set(cycle)
                    right_edges = set() if path is None else set(path)
                    draw_graph_counterexample(
                        left_ax, "G (input)", g, left_edges,
                        right_ax, "G' (output)", g_prime, right_edges
                    )
                    plt.suptitle(
                        "Counterexample: Expand test results for details\n")
                    save_plot(plt)

                    if bool(path):
                        Feedback.add_feedback("Your reduction does not work for the example shown above.\n"
                                              "G does not have a Hamiltonian cycle, but G' has a Hamiltonian path (highlighted in red).\n"
                                              "This violates the \"if and only if\" statement that we wrote in the previous question.")
                    else:
                        Feedback.add_feedback("Your reduction does not work for the example shown above.\n"
                                              "G has a Hamiltonian cycle (highlighted in red), but G' does not have a Hamiltonian path.\n"
                                              "This violates the \"if and only if\" statement that we wrote in the previous question.")
                    Feedback.set_score(0.1)
                    return
            except NameError as e:
                name = str(e).split("'")[1]
                if name == "G_prime":
                    Feedback.add_feedback(
                        "Your pseudocode tried to modify the graph without initializing G' first.")
                else:
                    Feedback.add_feedback(
                        f"Your pseudocode tried to access and/or modify the vertex '{name}' before defining it.")
                Feedback.set_score(0)
                return

        Feedback.set_score(1)
        return
