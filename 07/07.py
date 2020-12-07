#%%
import pandas as pd
import pyparsing as pp
import networkx as nx

# %%
bag_type_rule = pp.Group(pp.Word(pp.alphanums) + pp.Word(pp.alphanums) + pp.oneOf('bag bags').suppress()).addParseAction(lambda x: f'{x[0][0]} {x[0][1]}')
contains_rule = pp.Word(pp.nums)('n').addParseAction(lambda x: int(x[0])) + bag_type_rule('what')
rule = (
    bag_type_rule('what') + 
    pp.Literal('contain').suppress() + 
    pp.Group(pp.Or(
        pp.delimitedList(pp.Group(contains_rule)) |
        (pp.Suppress('no other bags'))
    ))('rule')
)

# %%
with open('input.txt', 'r') as f:
    df = pd.DataFrame({'raw': f.readlines()})
# %%
df['parsed'] = df['raw'].apply(rule.parseString)
df['edges_wo_no'] = df['parsed'].apply(lambda x: [(i.what, x.what) for i in x.rule])
df['edges_wgt'] = df['parsed'].apply(lambda x: [((x.what, i.what), i.n) for i in x.rule])
# %%
df
# %%
# part1
G = nx.DiGraph()
df['edges_wo_no'].apply(lambda x: [G.add_edge(e[0], e[1]) for e in x])
# %%
len(nx.single_source_shortest_path(G, 'shiny gold')) - 1  # 222


# %%
# part2
G = nx.DiGraph()
df['edges_wgt'].apply(lambda x: [G.add_edge(e[0], e[1], n=n) for e,n in x])
#%%
def count_p2(G, n):
    return 1 + sum([count_p2(G, k)*v['n'] for (k, v) in G[n].items()])
# %%
count_p2(G, 'shiny gold') - 1 # 13264
# %%
