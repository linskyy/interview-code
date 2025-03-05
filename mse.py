import numpy as np

def mse(y_true, y_pred):
    mse = np.mean(np.square(y_true - y_pred))
    return mse

y_true = np.array([1, 2, 3, 4])
y_pred = np.array([1.1, 1.9, 3.1, 3.8])
print("MSE:", mse(y_true, y_pred))