import numpy as np
import task2_2


def softmax(x):
        c = np.max(x)
        exp_x = np.exp(x - c)
        sum_exp_x = np.sum(np.exp(x - c), axis=1, keepdims=True)
        return exp_x / sum_exp_x

class MLP_3Layer:

    def __init__(self, W1, b1, W2, b2, W3, b3):
        self.network={}
        self.network['W1'] = W1
        self.network['W2'] = W2
        self.network['W3'] = W3
        self.network['b1'] = b1
        self.network['b2'] = b2
        self.network['b3'] = b3

    def forward(self,x):
        W1, W2, W3 = self.network['W1'], self.network['W2'], self.network['W3']
        b1, b2, b3 = self.network['b1'], self.network['b2'], self.network['b3']
        
        a1 = np.dot(x, W1) + b1
        z1 = task2_2.relu(a1)
        
        a2 = np.dot(z1, W2) + b2
        z2 = task2_2.relu(a2)

        a3 = np.dot(z2, W3) + b3
        z3 = softmax(a3)
        return z3

if __name__=='__main__':
    x = np.array([[1.0, 0.5], [-0.3, -0.2], [0.0, 0.8], [0.3, -0.4]])
    W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    b1 = np.array([0.1, 0.2, 0.3])
    W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    b2 = np.array([0.1, 0.2])
    W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
    b3 = np.array([0.1, 0.2])

    network = MLP_3Layer(W1, b1, W2, b2, W3, b3)
    print(network.forward(x))
