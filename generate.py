from pyknon.genmidi import Midi
from pyknon.music import NoteSeq

def generate(note,dur,outfile):
    print("Generating music file...")
    notes1 = NoteSeq(note)
    midi = Midi(1, tempo=90)
    midi.seq_notes(notes1, track=0)
    midi.write(outfile+".mid")