import numpy as np

class Affine:

    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        output = np.dot(x, self.W) + self.b
        return output

    def backward(self, dout):
        dx = np.dot(dout, W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        return dx, self.dW, self.db

if __name__=='__main__':
    x = np.array([[1.0, 0.5], [-0.4, 0.1]])
    W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]) 
    b = np.array([0.1, 0.2, 0.3])
    
    affine = Affine(W, b)
    output = affine.forward(x)

    print("順伝播出力:")
    print(output)

    dout = np.full(output.shape, 1.0)
    dx, dW, db = affine.backward(dout)
    print("逆伝播出力:")
    print(dx)

    print("逆伝播出力dW:")
    print(dW)

    print("逆伝播出力db:")
    print(db)

    
