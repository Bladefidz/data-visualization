import networkx as nx
import matplotlib.pyplot as plt
import community

try:
	import pygraphviz
	from networkx.drawing.nx_agraph import graphviz_layout
except ImportError:
	try:
		import pydot
		from networkx.drawing.nx_pydot import graphviz_layout
	except ImportError:
		raise ImportError("needs Graphviz and either "
						  "PyGraphviz or pydot")

G = nx.read_edgelist("data/ca-CSphd.txt",
						create_using = nx.Graph(),
						nodetype = int)

# Print information about graph
print(nx.info(G))
# Create network layout for visualizations
pos = graphviz_layout(G, prog='twopi', args='')
# Draw network graph
plt.axis("off")
nx.draw(G, pos = pos, cmap = plt.get_cmap("jet"),
		node_size = 35, with_labels = False)
ax = plt.gca() # to get the current axis
ax.collections[0].set_edgecolor("#202020")  # Set node's outline color
ax.collections[1].set_edgecolor("#7a7a7a")  # Set edge color
plt.show()