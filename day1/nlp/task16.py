import numpy as np
def cosine_sim(x1, x2):
    x1x2 = np.dot(x1, x2)
    x1_norm = np.linalg.norm(x1)
    x2_norm = np.linalg.norm(x2)
    return x1x2 /(x1_norm * x2_norm)

x1 = np.array([1, 0, 0, 1])
x2 = np.array([0, 1, 0, 1])
print(cosine_sim(x1, x2))
