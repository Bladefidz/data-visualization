from operator import itemgetter
import matplotlib.pyplot as plt
import networkx as nx

if __name__ == '__main__':
    # Create BA model graph
    n = 1000
    m = 2
    G = nx.generators.barabasi_albert_graph(n, m)
    node_and_degree = G.degree()
    (largest_hub, degree) = sorted(node_and_degree, key=itemgetter(1))[-1]
    
    # Create ego graph of main hub
    hub_ego = nx.ego_graph(G, largest_hub)

    # Draw graph
    pos = nx.spring_layout(hub_ego)
    nx.draw(hub_ego, pos, node_color='b', node_size=50, with_labels=False)

    # Draw ego as large and red
    nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], node_size=300,
                           node_color='r')
    plt.show()