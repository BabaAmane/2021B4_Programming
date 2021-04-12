import sys
import random

def random_word(word):
        if len(word) < 3:
            return word

        ##先頭と末尾以外ランダムにする
        temp_array = list(word[1:-1])
        random.shuffle(temp_array)
        output = word[0] + "".join(temp_array) + word[-1]
        return output


def typoglycemia(text):
    return " ".join(list(map(random_word, text.split())))

def main():
    command_len = len(sys.argv)
    for i in range(1,command_len):
        print(typoglycemia(sys.argv[i]), end=" ")

if __name__ == "__main__":
    main()

    
    
