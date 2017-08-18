def encrypt(path,key,outfile):
    print("\n-------Encrypting-------")
    plain_text = open(str(path),"r")
    for lines in plain_text:
        pt = lines
    scale = open("./scales/"+key,"r")
    enc = open("./encode/"+key+"_en","r")
    for notes in scale:
        note = notes
    print(pt)
    print(note+"\n")

    #variable only consists only 9(the last entry)
    #variable not getting initialized
    #check not working
    en = []
    i=0
    for lines in enc:
        en[i] = lines
        i = i+1