import generate
# import time

def encrypt(path,key,outfile):
    #timing the loops
    # program_starts = time.time()
    
    print("\n-------Encrypting-------")
    plain_text = open(str(path),"r")
    # scale = open("./scales/"+key,"r")
    encoding = open("./encode/"+key+"_en","r")
    duration = open("./encode/duration","r")
    cipher_text = open("c_text","w")
    cipher_dur = open("c_dur","w")
    #Getting plain text
    for lines in plain_text:
        pt = lines.upper()
    plain_text.close()
    
    #Creating list for the notes based on the key
    # note = []
    # for notes in scale:
    #     note.append(notes.rstrip('\n'))

    #Creating list for the encoding
    en = []
    for lines in encoding:
        en.append(lines.rstrip())

    #Creating list for the note duration
    dur = []
    for dura in duration:
        dur.append(dura.rstrip('\n'))

    #searching for note in the enc
    for let in pt:
        for letters in en:
            cipher_text.write(str(letters.find(let)).rstrip('-1'))
            for letter in letters:
                if letter == let:
                    cipher_dur.write(dur[en.index(letters)]+"\n")
                    break
                else:
                    continue
    cipher_text.close()
    cipher_dur.close()
    duration.close()
    encoding.close()
    # now = time.time()
    # taken = now - program_starts
    # print("Time taken",taken)
    generate.generate(key,outfile)