#%%
import numpy as np
from scipy.signal import convolve2d
# %%
def load_maps(fn):
    with open(fn) as f:
        res = [
            [
                (i == 'L') 
                for i in l.strip()
            ] 
            for l in f.readlines()
        ]
    return np.array(res, dtype=bool)

def print_map(seats, occupation):
    res = np.zeros_like(seats, dtype=str)
    res[:] = '.'
    res[seats] = 'L'
    res[occupation] = '#'

    print('\n'.join(''.join(i) for i in list(res)))

adj_mtx = np.array([[1,1,1], [1,0,1], [1,1,1]])

# %%
seats = load_maps('input.txt')
occupation = np.zeros_like(seats, dtype=bool)
print_map(seats, occupation)

# %%
while True:
    neighbours = convolve2d(occupation, adj_mtx, mode='same')

    new_occupation = (neighbours == 0) & (occupation == False) & seats
    left_occupation = (neighbours >= 4) & (occupation == True) & seats

    if not np.any(new_occupation | left_occupation):
        break

    occupation[new_occupation] = True
    occupation[left_occupation] = False

print_map(seats, occupation)
# %%
sum(sum(occupation)) # 2211
# %%
