def find_note(note,lineno):
    encoding = open("./encode/C_en","r")
    decode = open("output","w")
    word_list = []
    for line in encoding:
        l = line.strip().split('\n')
        word_list.append(l)

    if note == 60:
        print(word_list[lineno][0][0])

    elif note == 62:
        print(word_list[lineno][0][1])

    elif note == 64:
        print(word_list[lineno][0][2])

    elif note == 65:
        print(word_list[lineno][0][3])

    elif note == 67:
        print(word_list[lineno][0][4])

    elif note == 69:
        print(word_list[lineno][0][5])

    elif note == 71:
        print(word_list[lineno][0][6])