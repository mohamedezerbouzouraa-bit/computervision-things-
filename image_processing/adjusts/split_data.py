from load_data import data

target = data[:, -1]

bad = data[target <= 3]
mid = data[(target > 3) & (target < 7)]
good = data[target >= 7]

print(bad.shape, mid.shape, good.shape)
