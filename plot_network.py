import itertools
import time

import matplotlib.pyplot as plt
import networkx as nx

from generate_network import Social_Net
from spread import Spread_Net

N = 200

print("generating network...")
start = time.time()
SN = Social_Net(complete_net=False)
SN.set_parameters(ba_degree=2, social_prob=0.00025, rand_degree=25)
SN.start_network(N)
print(f"network generated in {time.time() - start}s")

G = SN.return_graph()

pos = nx.kamada_kawai_layout(G)

for w, e in itertools.product(range(2), repeat=2):
    nodelist = [n for n in G.nodes if G.nodes[n]["essential"] == e and G.nodes[n]["working"] == w]
    node_color = "tab:red" if w == 0 else "tab:blue"
    node_shape = "o" if e == 0 else "^"
    nx.draw_networkx_nodes(G, pos, nodelist=nodelist, node_color=node_color, node_shape=node_shape)

nx.draw_networkx_edges(G, pos, alpha=0.5)
edgelist = [e for e in G.edges if G.edges[e]["lockdown"] == 1]
nx.draw_networkx_edges(G, pos, edgelist=edgelist, edge_color="tab:green", width=4, alpha=0.5)

plt.show()