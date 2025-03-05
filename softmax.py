import numpy as np

def softmax(x):
    x = x - np.max(x)
    exp_value = np.exp(x)
    softmax_value = exp_value / np.sum(exp_value)
    return softmax_value

x = np.array([1,2,3,4])
res = softmax(x)
print(res)