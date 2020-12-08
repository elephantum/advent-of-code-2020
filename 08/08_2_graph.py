#%%
import pandas as pd
# %%
df = pd.read_csv('./input.txt', sep=' ', header=None, names=['op', 'arg'])
#%%
def run2(df):
    states = [(0, 0, [], False)]
    while True:
        new_states = []
        for ip, acc, visits, mod in states:
            if ip == len(df):
                return True, acc
            elif ip > len(df) or ip in visits:
                continue

            op = df.loc[ip, 'op']
            if op == 'acc':
                new_states.append((ip+1, acc+df.loc[ip, 'arg'], visits + [ip], mod))
            if op == 'jmp':
                new_states.append((ip+df.loc[ip, 'arg'], acc, visits + [ip], mod))
                if not mod:
                    new_states.append((ip+1, acc, visits + [ip], True))
            if op == 'nop':
                new_states.append((ip+1, acc, visits + [ip], mod))
                if not mod:
                    new_states.append((ip+df.loc[ip, 'arg'], acc, visits + [ip], True))
        states = new_states
# %%
%%time
run2(df) # 40ms

# %%
