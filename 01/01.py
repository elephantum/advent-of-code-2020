#%%
import pandas as pd
import numpy as np
# %%
data = pd.read_csv('input.txt', header=None, names=['n'])
# %%
data['sln'] = data['n'].apply(lambda n: len(np.where((data['n'] + n) == 2020)[0]) > 0)
# %%
data['sln']
# %%
data.index[data['sln']]
# %%
data.loc[data['sln'], 'n']
# %%
1084+936
# %%
1084*936
# %%


########

#%%
[(a, b, c) for a in data['n'] for b in data['n'] for c in data['n'] if a+b+c == 2020]
# %%
704 + 1223 + 93
# %%
704 * 1223 * 93
# %%
