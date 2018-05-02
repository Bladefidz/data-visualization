# https://www.udacity.com/wiki/creating-network-graphs-with-python
# A very, very simple plot

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):
    # Extract nodes from graph
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

    # Create networkx graph
    G = nx.Graph()

    # Add nodes
    for node in nodes:
        G.add_node(node)

    # Add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # Draw graph
    pos = nx.shell_layout(G)
    nx.draw(G, pos)

    # Show graph
    plt.show()


# Draw example
graph = [(20, 21),(21, 22),(22, 23), (23, 24),(24, 25), (25, 20)]
draw_graph(graph)