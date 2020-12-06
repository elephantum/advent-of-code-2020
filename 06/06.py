#%%
with open('input.txt', 'r') as f:
    data = f.read()

#%%
import pandas as pd

# %%
df = pd.DataFrame({'raw': data.split('\n\n')})
df['answers'] = df['raw'].apply(lambda x: [i for i in x.split('\n') if i != ''])
df['n_unique'] = df['raw'].apply(lambda x: len(set(x.replace('\n', ''))))
# %%
df
# %%
df['n_unique'].sum() #6530
# %%
def intersect(l):
    res = set(l[0])
    for i in l[1:]:
        res = res.intersection(set(i))
    return len(res)
# %%
df['n_intersect'] = df['answers'].apply(intersect)
# %%
df
# %%
df['n_intersect'].sum() #3323
# %%
