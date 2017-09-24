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
    
    #getting letters from plain text
    for letter in pt:
        for lines in en:
            for let in lines:
                if let == letter:
                    cipher_text.write(str(lines.index(let)))
                    cipher_dur.write(str(dur[en.index(lines)])+"\n")

    cipher_text.close()
    cipher_dur.close()
    duration.close()
    encoding.close()

    # now = time.time()
    # taken = now - program_starts
    # print("Time taken",taken)

    generate.generate(key,outfile)