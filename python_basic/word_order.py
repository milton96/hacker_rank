if __name__ == '__main__':
    words = {}
    #n = int(input().strip())
    f = open('words.txt')
    lines = f.readlines()
    
    for i in lines:
        try:
            word = i            
            if words.get(word):
                words[word] += 1
            else:
                words.setdefault(word, 1)
        except Exception as ex:
            print(ex)

    f.close()
    #print(words)
    values = list(words.values())
    print(len(list(words.keys())))
    print(' '.join(map(str, values)))
    