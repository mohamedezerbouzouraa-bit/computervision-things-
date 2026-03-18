import torch
from load_data import data
from compute_stats import data_mean, data_var

data_normalized = (data - data_mean) / torch.sqrt(data_var)

print(data_normalized[:5])
