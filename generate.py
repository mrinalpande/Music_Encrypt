from pyknon.genmidi import Midi
from pyknon.music import NoteSeq

def generate(notes,outfile):
    print("Generating music file...")
    notes1 = NoteSeq("A3 B3 C# D E F# G#")
    midi = Midi(1, tempo=90)
    midi.seq_notes(notes1, track=0)
    midi.write(outfile+".mid")