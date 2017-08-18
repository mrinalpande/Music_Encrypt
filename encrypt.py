def encrypt(path,key,outfile):
    print("\n-------Encrypting-------")
    plain_text = open(str(path),"r")
    for lines in plain_text:
        pt = lines.upper()
    print("\nChecking Scale...")
    scale = open("./scales/"+key,"r")
    enc = open("./encode/"+key+"_en","r")
    for notes in scale:
        note = notes
    print("Plain Text: "+pt)
    print("Notes on scale: "+note)
    en = []
    for lines in enc:
        en.append(lines.rstrip('\n'))