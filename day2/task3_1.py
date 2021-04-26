import numpy as np
class Multiply():
    def __init__(self):
    
        self.x = None
        self.y = None

    def forward(self, x, y):
    
        self.x = x
        self.y = y
        z = x * y
        return z

    def backprop(self, dz):
    
        dx = dz * self.y
        dy = dz * self.x
        return dx, dy


class Add():
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        z = x + y
        return z
    
    def backprop(self, dz):
        dx = dz * 1
        dy = dz * 1
        return dx, dy

if __name__=='__main__':
    a = 2
    b = 3
    c = 4
    add = Add()
    add_result = add.forward(a,b)
    mul = Multiply()
    mul_result = mul.forward(add_result, c)
    print("順伝播出力:",mul_result)
    
    dz = 1
    dab, dc = mul.backprop(dz)
    da, db = add.backprop(dab)

    print("逆伝播出力 da",da,"db:",db,"dc:",dc)



