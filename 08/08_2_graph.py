#%%
import pandas as pd
# %%
df = pd.read_csv('./input.txt', sep=' ', header=None, names=['op', 'arg'])
ops = list(df['op'])
args = list(df['arg'])
#%%
def run2(ops, args):
    states = [(0, 0, [], False)]
    while True:
        new_states = []
        for ip, acc, visits, mod in states:
            if ip == len(df):
                return True, acc
            elif ip > len(df) or ip in visits:
                continue

            op = ops[ip]
            if op == 'acc':
                new_states.append((ip+1, acc+args[ip], visits + [ip], mod))
            if op == 'jmp':
                new_states.append((ip+args[ip], acc, visits + [ip], mod))
                if not mod:
                    new_states.append((ip+1, acc, visits + [ip], True))
            if op == 'nop':
                new_states.append((ip+1, acc, visits + [ip], mod))
                if not mod:
                    new_states.append((ip+args[ip], acc, visits + [ip], True))
        states = new_states
# %%
%%time
run2(ops,args) # 5ms

# %%
