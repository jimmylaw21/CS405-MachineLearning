import torch.nn as nn
from torch import einsum
from .conv import Conv


class LinearTransformerLayer(nn.Module):

    def __init__(self, c):
        super().__init__()
        self.q = nn.Linear(c, c, bias=False)
        self.k = nn.Linear(c, c, bias=False)
        self.v = nn.Linear(c, c, bias=False)
        self.fc1 = nn.Linear(c, c, bias=False)
        self.fc2 = nn.Linear(c, c, bias=False)

    def forward(self, x):
        q = self.q(x)
        k = self.k(x)
        v = self.v(x)
        dim = q.shape[-1]
        q = q.softmax(dim=-1)
        k = k.softmax(dim=-2)
        q = q * dim ** -0.5
        context = einsum('cnd,cne->cde', k, v)
        attn = einsum('cnd,cde->cne', q, context)
        attn = attn.reshape(*q.shape)
        x = attn + x
        return self.fc2(self.fc1(x)) + x


class LinearTransformerBlock(nn.Module):

    def __init__(self, c1, c2, num_layers):
        super().__init__()
        self.conv = None
        if c1 != c2:
            self.conv = Conv(c1, c2)
        self.linear = nn.Linear(c2, c2)  # learnable position embedding
        self.tr = nn.Sequential(*(LinearTransformerLayer(c2) for _ in range(num_layers)))
        self.c2 = c2

    def forward(self, x):
        if self.conv is not None:
            x = self.conv(x)
        b, _, w, h = x.shape
        p = x.flatten(2).permute(2, 0, 1)
        return self.tr(p + self.linear(p)).permute(1, 2, 0).reshape(b, self.c2, w, h)
