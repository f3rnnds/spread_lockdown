import random
import time

import networkx as nx

from generate_network import Social_Net
from spread import Spread_Net

N = 10000
network_file = "results/network.graphml"

print("generating network...")
start = time.time()
SN = Social_Net(complete_net=False)
SN.set_parameters(ba_degree=2, social_prob=0.00025, rand_degree=25)
SN.start_network(N)
print(f"network generated in {time.time() - start}s")

# print("plot degree distribution")
# SN.degree_histogram()

G = SN.return_graph()

# print("save network")
# nx.write_graphml(G, network_file)

# print("load network")
# G = nx.read_graphml(network_file)

infected = random.sample(list(G.nodes), 5)
bfs = nx.bfs_layers(G, infected)
max_depth = len(dict(enumerate(bfs)))
print(f"max depth: {max_depth}")