import generate

def encrypt(path,key,outfile):
    print("\n-------Encrypting-------")
    plain_text = open(str(path),"r")
    for lines in plain_text:
        pt = lines.upper()
    print("\nChecking Scale...")
    scale = open("./scales/"+key,"r")
    encoding = open("./encode/"+key+"_en","r")
    duration = open("./encode/duration","r")

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
    print(note[2])
    print(en)
    print(dur[4])


    #generate.generate(note,dur,outfile)
    #check encoding
    # for word in pt:
    #     if word in en:
    #         ind = en.index(word)
    #         print(ind)