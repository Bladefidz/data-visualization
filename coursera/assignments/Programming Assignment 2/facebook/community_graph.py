import networkx as nx
import matplotlib.pyplot as plt
import community


G_fb = nx.read_edgelist("data/facebook_combined.txt",
						create_using = nx.Graph(),
						nodetype = int)

# Print information about graph
print(nx.info(G_fb))
# Create network layout for visualizations
spring_pos = nx.spring_layout(G_fb)
# Find best partition to identify communities
parts = community.best_partition(G_fb)
values = [parts.get(node) for node in G_fb.nodes()]
# Draw network graph
plt.axis("off")
nx.draw(G_fb, pos = spring_pos, cmap = plt.get_cmap("jet"),
		node_color = values, node_size = 35, with_labels = False)
ax = plt.gca() # to get the current axis
ax.collections[0].set_edgecolor("#202020")  # Set node's outline color
ax.collections[1].set_edgecolor("#7a7a7a")  # Set edge color
plt.show()