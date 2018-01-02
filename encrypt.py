import generate

def encrypt(path,key,outfile):
    print("\n-------Encrypting-------")
    plain_text = open(str(path),"r")
    encoding = open("./encode/"+"C_en","r")
    duration = open("./encode/duration","r")
    cipher_text = open("c_text","w")
    cipher_dur = open("c_dur","w")

    #Getting plain text
    for lines in plain_text:
        pt = lines.upper()
    plain_text.close()

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
                    if lines.index(let) == 0:
                        cipher_text.write(str(lines.index(let))+"\n")
                    elif lines.index(let) == 1:
                        cipher_text.write(str(lines.index(let)+1)+"\n")
                    elif lines.index(let) == 2 or lines.index(let) == 3:
                        cipher_text.write(str(lines.index(let)+2)+"\n")
                    elif lines.index(let) == 4:
                        cipher_text.write(str(lines.index(let)+3)+"\n")
                    elif lines.index(let) == 5:
                        cipher_text.write(str(lines.index(let)+4)+"\n")
                    elif lines.index(let) == 6:
                        cipher_text.write(str(lines.index(let)+5)+"\n")
                    cipher_dur.write(str(dur[en.index(lines)])+"\n")

    cipher_text.close()
    cipher_dur.close()
    duration.close()
    encoding.close()
    generate.generate(key,outfile)