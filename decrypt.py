import mido
from mido import MidiFile
import note_find as find_note


def decrypt(path,key):
    note_dur = open("parts","w")

    mid  = MidiFile(''+path+'')

    msg_lst = []
    note_lst = []

    for i,track in enumerate(mid.tracks):
        for msg in track:
            msg_lst.append(str(msg))
            if msg.type == 'key_signature':
                m = str(msg)
                k = m[33]
    if(k!=key):
        print("Key doesn't match.")
        exit(0)

    #getting the notes and duration
    for al in msg_lst:
        if al.find("note_off")==0:
            parts = al.split(" ")
            note_dur.write(parts[2]+","+parts[4]+"\n")
    note_dur.close()

    note_dur =open("parts","r")

    for notes in note_dur:
        note = int(notes[5]+notes[6])
        dur = int(notes[13]+notes[14]+notes[15])

        if dur == 512:
            find_note.find_note(note,0)
        elif dur == 256:
            find_note.find_note(note,1)

        elif dur ==128:
            find_note.find_note(note,2)

        elif dur == 64:
            find_note.find_note(note,3)