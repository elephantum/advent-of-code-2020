#%%
import numpy as np
import networkx as nx
# %%
input_data = np.genfromtxt('./input.txt', dtype=int)
input_data.sort()
start = 0
end = np.max(input_data) + 3

#%%
data = np.append([start, end], input_data)
data.sort()
np.unique(data[1:] - data[:-1], return_counts=True)
#%%
75*32

#%%
G = nx.DiGraph()

G.add_node(start)
for i in input_data:
    for j in range(1, 4):
        if (i-j) in G:
            G.add_edge(i-j, i)
G.add_edge(end - 3, end)

# %%
%%time

pi = 0
ways = 1
for i in range(1, len(data)):
    if data[i] - data[i-1] == 3:
        segment_ways = sum(1 for i in nx.all_simple_paths(G, data[pi], data[i-1]))
        print(data[pi], data[i-1], segment_ways)
        ways *= segment_ways
        pi = i-1

# %%
ways # 338510590509056
# %%
