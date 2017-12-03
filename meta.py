from mido import MetaMessage, MidiTrack, MidiFile
import os

def meta(file,  key, out):
    #adding the key to the file
    mid = MidiFile(file)
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(MetaMessage('key_signature', key=''+key+''))
    mid.save(''+out+'.mid')
    os.remove("inter.mid")