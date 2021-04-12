
def terms(list_x):
    terms = []
    temp_list = sum(list_x,[])
    for i in range(len(temp_list)):
        if temp_list[i] not in terms:
            terms.append(temp_list[i])
      
    return terms

def main():
    f = open('./dataset/data.txt','r')
    docs = []
    while True:
        data = f.readline().rstrip('\n')
        if data:
            docs.append(data.split('と'))
        else:
            break

    print(docs)
    print(terms(docs))

if __name__ == "__main__":
    main()

    