from pyknon.genmidi import Midi
from pyknon.music import Note
import meta
import os

def generate(key,outfile):
    # scale = open("./scales/"+key,"r")
    cipher = open("c_text","r")
    dur = open("c_dur","r")

    notes1=[]
    #using for getting the data and creating lits.
    while True:
        ci = cipher.readline()
        du = dur.readline()
        if not ci or not du:
            break
        c = int(ci)
        d = float(du)
        notes1.append(Note(value=c,dur = d))

    for note in notes1:
        print(note)

    midi = Midi(1,tempo=80)
    midi.seq_notes(notes1,track=0)
    midi.write("inter.mid")
    cipher.close()
    dur.close()
    os.remove("c_text")
    os.remove("c_dur")
    meta.meta("inter.mid",key,outfile)

