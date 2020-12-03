#%%
import pandas as pd
# %%
data = pd.read_csv('input.txt', sep=': ', header=None, names=['rule', 'pwd'])
# %%
data
# %%
data['c'] = data['rule'].apply(lambda x: x.split(' ')[1])
# %%
data
# %%
data['min'] = data['rule'].apply(lambda x: int(x.split(' ')[0].split('-')[0]))
data['max'] = data['rule'].apply(lambda x: int(x.split(' ')[0].split('-')[1]))
# %%
data
# %%
data['actual'] = data.apply(lambda x: sum(1 for i in x['pwd'] if i == x['c']), axis='columns')
# %%
data['ok'] = (data['actual'] >= data['min']) & (data['actual'] <= data['max'])
# %%
data
# %%
sum(data['ok'])
#591

#%%
def get_chr(s, n):
    if len(s) >= n:
        return s[n-1]
    return None

data['ok2'] = data.apply(lambda x: (get_chr(x['pwd'], x['min']) == x['c']) ^ (get_chr(x['pwd'], x['max']) == x['c']), axis='columns')
# %%
sum(data['ok2'])
# 335
# %%
