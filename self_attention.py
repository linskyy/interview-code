import torch
import torch.nn as nn
import numpy as np
class SelfAttention(nn.Module):
    def __init__(self, input_dim, dim_k, dim_v):
        super().__init__()
        self.q = nn.Linear(input_dim, dim_k)
        self.k = nn.Linear(input_dim, dim_k)
        self.v = nn.Linear(input_dim, dim_v)
        self.softmax = nn.Softmax(dim=-1)
        self.norm = 1 / np.sqrt(dim_k)
    
    def forward(self, x):
        Q = self.q(x)
        K = self.k(x)
        V = self.v(x)
        attn = self.softmax(torch.bmm(Q, K.permute(0,2,1)) / self.norm) 
        output = torch.bmm(attn, V)
        return output
    

X = torch.randn(4,3,2)
self_attention = SelfAttention(2,4,5)
res = self_attention(X)
print(res.shape)