import sys

def n_gram(text, n):
    output = []
    for idx in range(len(text) - n + 1):
        output.append(text[idx:idx + n])

    return output


def main():
    command_len = len(sys.argv)
    word = []
    text_sum = ""

    for i in range(1,command_len):
        text_sum += sys.argv[i]
        word.append(sys.argv[i])

    text = ' '.join(word)
    words = text.split(' ')
    
    print("単語bi-gram:",n_gram(words,2))
    print("文字bi-gram:",n_gram(text_sum,2))

if __name__ == "__main__":
    main()

    
