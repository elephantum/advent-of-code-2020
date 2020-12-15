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

# %%
seats = load_maps('input.txt')

#%%
occupation = np.zeros_like(seats, dtype=bool)
print_map(seats, occupation)

#%%
adj_mtx = np.array([[1,1,1], [1,0,1], [1,1,1]])    
def count_neighbours(seats, occupation):
    neighbours = convolve2d(occupation, adj_mtx, mode='same')
    return neighbours

# %%
while True:
    neighbours = count_neighbours(seats, occupation)
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
occupation = np.zeros_like(seats, dtype=bool)
print_map(seats, occupation)

#%%
def get_adj(seats, i, j):
    adj = []
    for di, dj in [(-1,-1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
        k = 1
        imax, jmax = seats.shape
        while True:
            ik = i + di*k
            jk = j + dj*k
            if ik < 0 or ik >= imax:
                break
            if jk < 0 or jk >= jmax:
                break
            if seats[ik, jk]:
                adj.append((ik, jk))
                break
            k += 1
    return adj

def count_neighbours2(seats, occupation):
    imax, jmax = seats.shape

    neighbours = np.zeros_like(occupation, dtype=int)

    for i in range(imax):
        for j in range(jmax):
            c = 0
            for ni, nj in get_adj(seats, i, j):
                if occupation[ni, nj]:
                    c +=1
            neighbours[i, j] = c
    
    return neighbours

# %%
occupation = np.zeros_like(seats, dtype=bool)
while True:
    neighbours = count_neighbours2(seats, occupation)
    new_occupation = (neighbours == 0) & (occupation == False) & seats
    left_occupation = (neighbours >= 5) & (occupation == True) & seats

    if not np.any(new_occupation | left_occupation):
        break

    occupation[new_occupation] = True
    occupation[left_occupation] = False

#%%
print_map(seats, occupation)

# %%
sum(sum(occupation)) #1995
# %%
