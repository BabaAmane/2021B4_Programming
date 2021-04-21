import task1_1

if __name__=='__main__':
    AND = task1_1.Perception(1, 1, 2)
    NAND = task1_1.Perception(-1, -1.5, -2)
    OR = task1_1.Perception(1, 1, 0.5)

    x1_list = [1, 1, 0, 0]
    x2_list = [1, 0, 1, 0]

    for i in range(len(x1_list)):
        s1 = NAND.forward(x1_list[i], x2_list[i])
        s2 = OR.forward(x1_list[i], x2_list[i])
        xor = AND.forward(s1, s2)
        
        print("XOR(%d, %d) = %d " %(x1_list[i],x2_list[i],xor))
