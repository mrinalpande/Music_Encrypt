from pyknon.genmidi import Midi
from pyknon.music import Note

def generate(key,outfile):
    # scale = open("./scales/"+key,"r")
    cipher = open("c_text","r")
    dur = open("c_dur","r")

    notes1=[]
    #using for getting the data and creating lits.
    # todo get durations similarly 
    while True:
        ci = cipher.read(1)
        du = dur.readline()
        if not ci or not du:
            break
        c = int(ci)
        # print(du)
        # print(type(du))
        d = float(du)
        notes1.append(Note(value=c,dur = d))

    midi = Midi(1,tempo=80)
    midi.seq_notes(notes1,track=0)
    midi.write("gen.mid")