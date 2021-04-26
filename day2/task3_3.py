import numpy as np

class Softmax:

    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out

    def backward(self, dout):
        dx = dout * (1 - self.out) * self.out
        return dx

if __name__=='__main__':
    x = np.array([-0.5, 0.0, 1.0, 2.0]) 
    softmax = Softmax()
    output = softmax.forward(x)
    print("順伝播:", output)

    dout = np.full(output.shape, 1.0)
    backward_output = softmax.backward(dout)
    print("逆伝播出力:",backward_output)