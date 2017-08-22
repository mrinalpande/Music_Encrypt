import generate

def encrypt(path,key,outfile):
    print("\n-------Encrypting-------")
    plain_text = open(str(path),"r")
    scale = open("./scales/"+key,"r")
    encoding = open("./encode/"+key+"_en","r")
    duration = open("./encode/duration","r")

    #Getting plain text
    for lines in plain_text:
        pt = lines.upper()

    #Creating list for the notes based on the key
    note = []
    for notes in scale:
        note.append(notes.rstrip('\n'))

    #Creating list for the encoding
    en = []
    for lines in encoding:
        en.append(lines.rstrip())

    #Creating list for the note duration
    dur = []
    for dura in duration:
        dur.append(dura.rstrip('\n'))

    #Checking
    # print(note[2])
    # print(en)
    # print(dur[4])

    i=0
    while i < len(pt):
        print(en[0])
        if pt[i] in en[0][1]:
            print(pt[i])
            print(en.index(pt[i]))
        i = i+1

    #generate.generate(note,dur,outfile)
    #check encoding
    # for word in pt:
    #     if word in en:
    #         ind = en.index(word)
    #         print(ind)