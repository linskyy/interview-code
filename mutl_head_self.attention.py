import torch
import torch.nn as nn
import numpy as np

class MHSA(nn.Module):
    def __init__(self, input_dim, dim_k, dim_v, head):
        super().__init__()
        self.head = head
        self.q = nn.Linear(input_dim, dim_k * head)
        self.k = nn.Linear(input_dim, dim_k * head)
        self.v = nn.Linear(input_dim, dim_v * head)
        self.norm = 1 / np.sqrt(dim_k)
    
    def forward(self, x):
        Q = self.q(x) #[bs, T, head * dim_k]
        K = self.k(x) #[bs, T, head * dim_k]
        V = self.v(x) #[bs, T, head * dim_v]
        Q = Q.reshape(Q.size()[0], Q.size()[1], self.head, -1).permute(0,2,1,3) #[bs, head, T, dim_k]
        K = K.reshape(K.size()[0], K.size()[1], self.head, -1).permute(0,2,1,3) #[bs, head, T, dim_k]
        V = V.reshape(V.size()[0], V.size()[1], self.head, -1).permute(0,2,1,3) #[bs, head, T, dim_v]
        attn = nn.Softmax(dim=-1)(torch.matmul(Q, K.permute(0,1,3,2)) * self.norm) #[bs, head, T, T]
        output = torch.matmul(attn, V) #[bs, head, T, dim_v]
        output = output.permute(0,2,3,1)
        output = output.reshape(output.size()[0], output.size(1), -1) #[bs, T, dim_v*head]
        return output

X = torch.randn(64,16,4)
multi = MHSA(4, 2, 3, 8)
y = multi(X)
print(y.shape)
