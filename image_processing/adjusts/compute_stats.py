import torch
from load_data import data

data_mean = torch.mean(data, dim=0)
data_var = torch.var(data, dim=0)

print("Mean:\n", data_mean)
print("Variance:\n", data_var)
