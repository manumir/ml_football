#! /usr/bin/python3

import torch
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv('finall.csv')
data=data[:5000]

y=data.pop('result')
print(y)
x=data
x, x_test, y, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42)

x,y= np.array(x), np.array(y)
x,y= torch.from_numpy(x), torch.from_numpy(y)
x,y= x.float(), y.float()

D_in, H, D_out = 6, 25, 1

model = torch.nn.Sequential(
    torch.nn.Linear(D_in, H),
    torch.nn.ReLU(),
    torch.nn.Linear(H, D_out),
    )

loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-1
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
for t in range(500):
    # Forward pass: compute predicted y by passing x to the model.
    y_pred = model(x)

    # Compute and print loss.
    loss = loss_fn(y_pred, y)
    print(t, loss.item())

    # Before the backward pass, use the optimizer object to zero all of the
    # gradients for the variables it will update (which are the learnable
    # weights of the model). This is because by default, gradients are
    # accumulated in buffers( i.e, not overwritten) whenever .backward()
    # is called. Checkout docs of torch.autograd.backward for more details.
    optimizer.zero_grad()

    # Backward pass: compute gradient of the loss with respect to model
    # parameters
    loss.backward()

    # Calling the step function on an Optimizer makes an update to its
    # parameters
    optimizer.step()

x_test= np.array(x_test)
x_test= torch.from_numpy(x_test)
x_test= x_test.float()

y_tested=model(x_test)
#acc=accuracy_score(y_test,y_tested)
print(y_tested)
#print('acc: ',acc)

