import numpy as np

def relu(x):
    return np.maximum(0, x)

if __name__=='__main__':
    x = np.array([-1.0, 0.0, 0.5, 2.0])
    print(relu(x))