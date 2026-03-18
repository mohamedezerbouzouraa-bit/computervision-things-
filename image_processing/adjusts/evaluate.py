import torch
from load_data import data
from threshold_model import predicted

target = data[:, -1]
actual = target > 5

matches = torch.sum(actual & predicted).item()
n_pred = torch.sum(predicted).item()
n_actual = torch.sum(actual).item()

print("Matches:", matches)
print("Precision:", matches / n_pred)
print("Recall:", matches / n_actual)
