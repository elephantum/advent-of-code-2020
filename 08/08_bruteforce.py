#%%
import pandas as pd
# %%
df = pd.read_csv('input.txt', sep=' ', header=None, names=['op', 'arg'])
# %%
def run(df):
    df['visit'] = 0
    ip = 0
    acc = 0

    while True:
        if ip == len(df):
            return True, acc
        if ip > len(df) or df.loc[ip, 'visit'] == 1:
            return False, acc

        df.loc[ip, 'visit'] += 1

        if df.loc[ip, 'op'] == 'acc':
            acc += df.loc[ip, 'arg']
            ip += 1
        elif df.loc[ip, 'op'] == 'jmp':
            ip += df.loc[ip, 'arg']
        elif df.loc[ip, 'op'] == 'nop':
            ip += 1
# %%
%%time
for ip in range(len(df)):
    if df.loc[ip, 'op'] == 'jmp':
        df_test = df.copy()
        df_test.loc[ip, 'op'] = 'nop'
    elif df.loc[ip, 'op'] == 'nop':
        df_test = df.copy()
        df_test.loc[ip, 'op'] = 'jmp'
    else:
        continue

    (ok, acc) = run(df_test)
    if ok:
        break
# %%
# 7.67sec
ip, ok, acc
# %%
