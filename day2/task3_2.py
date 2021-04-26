import numpy as np

class Relu:

    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx

if __name__=='__main__':
    x = np.array([-0.5, 0.0, 1.0, 2.0]) 
    relu = Relu()
    output = relu.forward(x)
    print("順伝播:", output)

    dout = np.full(output.shape, 1.0)
    backward_output = relu.backward(dout)
    print("逆伝播出力:",backward_output)