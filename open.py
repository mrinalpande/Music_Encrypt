from mido import MidiFile

mid  = MidiFile('outfile.mid')

for i,track in enumerate(mid.tracks):
        # print('Track {}:{}'.format(i,track.name))
        for msg in track:
            if msg.type == 'key_signature':
                m = str(msg)
                print(m[33])
