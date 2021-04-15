input = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

##1,5,6,7,8,9,15,16,19の時は最初の1文字ｊ esle2文字
list1 = []
list2 = [1,5,6,7,8,9,15,16,19]
for word in input.split():
    list1.append(word.strip(",."))

dic = {}
for i in range(len(list1)):
    if i+1 in list2:
        dic[i+1] = list1[i][:1]
    else:
        dic[i+1] = list1[i][:2]

print(dic)


