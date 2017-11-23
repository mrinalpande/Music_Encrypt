import mido
from mido import MidiFile

def decrypt(path,key):
    mid  = MidiFile(''+path+'')
    encoding = open("./encode/C_en","r")
    msg_lst = []
    note_lst = []
    for i,track in enumerate(mid.tracks):
        print('Track {}:{}'.format(i,track.name))
        for msg in track:
            msg_lst.append(str(msg))
            if msg.type == 'key_signature':
                m = str(msg)
                k = m[33]
    if(k!=key):
        print("Key doesn't match.")
        exit(0)

    for words in encoding:
        print(words[0])


    for al in msg_lst:
        if al.find("note_off")==0:
            print(al)