import numpy as np
import task2_5

def cross_entropy_error(y, t):
    return -np.sum(t * np.log(y))

class SoftmaxCrossEntropy:

    def __init__(self):
        self.loss = None ##損失
        self.y = None ##出力softmax
        self.t = None ##教師データ


    def forward(self, x, t):
        self.t = t
        self.y = task2_5.softmax(x)
        self.loss = cross_entropy_error(self.y, self.t) / len(x)
        return self.loss

    def backward(self):
        
        dx = self.y - self.t
        return dx


    

if __name__=='__main__':

    x = np.array([[1.0, 0.5], [-0.4, 0.1]])
    t = np.array([[1.0, 0.0], [0.0, 1.0]])
    soft_max_with_loss = SoftmaxCrossEntropy()
    output = soft_max_with_loss.forward(x, t)

    print("順伝播出力:")
    print(output)

    print("逆伝播出力:")
    print(soft_max_with_loss.backward())

    

