from pyknon.genmidi import Midi
from pyknon.music import Note

notes1 = [Note(value=0, octave=4).transposition(9),Note(value=2, octave=4).transposition(9)]
print(notes1)
midi = Midi(1, tempo=80)
midi.seq_notes(notes1, track=0)
midi.write("demo.mid")