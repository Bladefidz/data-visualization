import networkx as nx
import matplotlib.pyplot as plt

G_fb = nx.read_edgelist("data/facebook_combined.txt",
						create_using = nx.Graph(),
						nodetype = int)
# Print information about graph
print(nx.info(G_fb))
# Create network layout for visualizations
spring_pos = nx.spring_layout(G_fb)
# Draw network graph
plt.axis("off")
nx.draw(G_fb, pos=spring_pos, with_labels=False, node_size=35)
ax = plt.gca() # to get the current axis
ax.collections[0].set_edgecolor("#202020")  # Set node's outline color
ax.collections[1].set_edgecolor("#7a7a7a")  # Set edge color
plt.show()