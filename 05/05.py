#%%
import pandas as pd

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
df['n'] = df['code'].apply(ticket_to_n)

# %%
### part 1
df['n'].max() # 998

# %%
### part 2
tt = df['n'].sort_values().to_numpy()
tt[:-1][tt[:-1] +2 == tt[1:]] #675 - это ближайший снизу сосед
# %%
675 in tt # true
# %%
676 in tt # false
# %%
677 in tt # true
# %%
