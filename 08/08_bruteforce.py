#%%
import pandas as pd
# %%
df = pd.read_csv('./08/input.txt', sep=' ', header=None, names=['op', 'arg'])
ops = list(df['op'])
args = list(df['arg'])
# %%
def run(ops, args):
    visits = list([0] * len(ops))
    ip = 0
    acc = 0

    while True:
        if ip == len(ops):
            return True, acc
        if ip > len(ops) or visits[ip] == 1:
            return False, acc

        visits[ip] += 1

        if ops[ip] == 'acc':
            acc += args[ip]
            ip += 1
        elif ops[ip] == 'jmp':
            ip += args[ip]
        elif ops[ip] == 'nop':
            ip += 1
#%%
run(ops, args)
#%%
%%time
for ip in range(len(ops)):
    if ops[ip] == 'jmp':
        ops_test = ops.copy()
        ops_test[ip] = 'nop'
    elif ops[ip] == 'nop':
        ops_test = ops.copy()
        ops_test[ip] = 'jmp'
    else:
        continue

    (ok, acc) = run(ops_test, args)
    if ok:
        break
# %%
# 11.2ms
ip, ok, acc
# %%
