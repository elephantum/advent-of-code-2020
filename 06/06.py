#%%
import pandas as pd

#%%
with open('input.txt', 'r') as f:
    data = f.read()

# %%
df = pd.DataFrame({'raw': data.split('\n\n')})
df['answers'] = df['raw'].apply(lambda x: [i for i in x.split('\n') if i != ''])

# %%
### part 1
df['n_unique'] = df['raw'].apply(lambda x: len(set(x.replace('\n', ''))))
df['n_unique'].sum() #6530

# %%
### part 2
df['n_intersect'] = df['answers'].apply(lambda x: len(set.intersection(*[set(i) for i in x])))
df['n_intersect'].sum() #3323

# %%
