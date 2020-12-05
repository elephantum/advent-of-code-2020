#%%
import pandas as pd

#%%
test = [
    ('BFFFBBFRRR', 567),
    ('FFFBBBFRRR', 119),
    ('BBFFBBFRLL', 820)
]
#%%
def ticket_to_n(s):
    return int(
        s\
            .replace('B', '1')\
            .replace('F', '0')\
            .replace('R', '1')\
            .replace('L', '0'), 2
    )
#%%
with open('input.txt') as f:
    data = [l.strip() for l in f.readlines()]

#%%
df = pd.DataFrame({'code': data})
# %%
df
# %%
df['n'] = df['code'].apply(ticket_to_n)
# %%
df
# %%
df['n'].max() # 998
# %%
tt = df['n'].sort_values().to_numpy()
# %%
tt[:-1][tt[:-1] +2 == tt[1:]]
# %%
675 in tt
# %%
676 in tt
# %%
676 in tt
# %%
