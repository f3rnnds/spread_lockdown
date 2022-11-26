import networkx as nx
import time

print("loading network...")
start = time.time()
G = nx.read_graphml("results/network_160k.graphml") # 331M
print(f"network loaded in {time.time() - start}s")

print("saving gexf...")
nx.write_gexf(G, "results/network_160k.gexf") # 592M
print("saving gml...")
nx.write_gml(G, "results/network_160k.gml") # 238M
print("saving pickle...")
nx.write_gpickle(G, "results/network_160k.pickle") # 105M