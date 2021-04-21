import task1_1

if __name__=='__main__':
    AND = task1_1.Perception(1, 1, 2)
    NAND = task1_1.Perception(-1, -1.5, -2)
    OR = task1_1.Perception(1, 1, 0.5)

    x1_list = [1, 1, 0, 0]
    x2_list = [1, 0, 1, 0]

    for i in range(len(x1_list)):
         print("AND(%d, %d) = %d " %(x1_list[i],x2_list[i],AND.forward(x1_list[i],x2_list[i])) , end = '')
         print("NAND(%d, %d) = %d " %(x1_list[i],x2_list[i],NAND.forward(x1_list[i],x2_list[i])) , end = '')
         print("OR(%d, %d) = %d " %(x1_list[i],x2_list[i],OR.forward(x1_list[i],x2_list[i])))


    

     