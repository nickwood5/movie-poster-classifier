import torch

train_data = []

x_data = [1, 2, 3, 4]
labels = [["12", "3"], ["3", "4"], ["9", "20"], ["45", "33"]]

for i in range(len(x_data)):
   train_data.append([x_data[i], labels[i]])

trainloader = torch.utils.data.DataLoader(train_data, shuffle=True, batch_size=100)
i1, l1 = next(iter(trainloader))
print(i1.shape)

print(i1)
print(l1)