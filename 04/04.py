#%%
import pandas as pd

with open('input.txt', 'r') as f:
    data = f.read()

# %%
df = pd.DataFrame.from_records(
    [{j.split(':')[0]: j.split(':')[1] for j in i.replace('\n', ' ').split(' ')} for i in data.strip().split('\n\n')],
    coerce_float=False
)
df = df.fillna('')

#%%
sum((df['byr'] != '') & (df['iyr'] != '') & (df['eyr'] != '') & (df['hgt'] != '') & (df['hcl'] != '') & (df['ecl'] != '') & (df['pid'] != ''))
# part1 = 230

# %%
def validate_int(min,max):
    def validate(s):
        try:
            i = int(s)
            return i >= min and i <= max
        except:
            return False
    return validate

validate_hgt_in = validate_int(59, 76)
validate_hgt_cm = validate_int(150, 193)

def validate_hgt(s):
    if not isinstance(s, str):
        return False
    elif s.endswith('in'):
        return validate_hgt_in(s[:-2])
    elif s.endswith('cm'):
        return validate_hgt_cm(s[:-2])
    else:
        return False

# %%
df['iyr_valid'] = df['iyr'].apply(validate_int(2010, 2020))
df['byr_valid'] = df['byr'].apply(validate_int(1920, 2002))
df['eyr_valid'] = df['eyr'].apply(validate_int(2020, 2030))
df['hgt_valid'] = df['hgt'].apply(validate_hgt)
df['hcl_valid'] = df['hcl'].str.match(r'^#([0-9]|[a-f]){6}$')
df['ecl_valid'] = df['ecl'].str.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
df['pid_valid'] = df['pid'].str.match(r'^\d{9}$')

df['valid'] = (
    df['iyr_valid'] &
    df['byr_valid'] &
    df['eyr_valid'] &
    df['hgt_valid'] &
    df['hcl_valid'] &
    df['ecl_valid'] &
    df['pid_valid'] 
)

df
# %%
sum(df['valid'])

# part2 = 156

# %%
