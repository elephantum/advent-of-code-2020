#%%
with open('input.txt', 'r') as f:
    data = [
        i.strip()
        for i in f.readlines()
    ]

# %%
data
# %%
x = 0
dx = 3

# %%
def cnt_slope(dx,dy):
    y = 0
    x = 0
    w = len(data[0])
    cnt = 0
    while y < len(data):
        if data[y][x % w] == '#':
            cnt += 1
        y += dy
        x += dx

    return cnt
# %%
cnt_slope(3, 1)
# 272
# %%
[
    cnt_slope(dx,dy)
    for (dx,dy) in [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
    ]
]
# %%
85 * 272 * 66 * 73 * 35
# %%
