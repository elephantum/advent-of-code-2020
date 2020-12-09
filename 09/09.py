#%%
with open('input.txt', 'r') as f:
    data = [int(i) for i in f.readlines()]
# %%
def is_sum(x, nn):
    for i_n, i in enumerate(nn):
        for j in nn[i_n+1:]:
            if i+j == x:
                return True
    return False
# %%
WINDOW=25
for i in range(WINDOW, len(data)):
    if not is_sum(data[i], data[i-WINDOW:i]):
        print(data[i])
        break
# 731031916

# %%
X = 731031916
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if sum(data[i:j]) == X:
            print(data[i:j])
# [30684790, 31929175, 33239826, 37982233, 32111531, 35048416, 34484211, 34933587, 53564537, 35733886, 53833200, 37317716, 62711937, 51019481, 51993598, 52688226, 61755566]
# %%
res = [30684790, 31929175, 33239826, 37982233, 32111531, 35048416, 34484211, 34933587, 53564537, 35733886, 53833200, 37317716, 62711937, 51019481, 51993598, 52688226, 61755566]
# %%
min(res) + max(res)
# %%
