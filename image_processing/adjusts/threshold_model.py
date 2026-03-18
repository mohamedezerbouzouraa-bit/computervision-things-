from load_data import data

target = data[:, -1]
total_sulfur = data[:, 6]

threshold = 141.83

predicted = total_sulfur < threshold

print(predicted[:10])
