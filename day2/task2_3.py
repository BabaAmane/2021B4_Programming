import numpy as np
import task2_2

class SingleLayer:
    def __init__(self, x, W, b):
        self.x = x
        self.W = W
        self.b = b
    
    def calc(self):
        return task2_2.relu(np.dot(W.T, x)+b)


if __name__=='__main__':
    x = np.array([1.0, 0.5])
    W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    b = np.array([0.1, 0.2, 0.3])
    single_layer = SingleLayer(x,W,b)
    output = single_layer.calc()
    print(output)