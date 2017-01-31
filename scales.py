from musthe import Note, Interval, scale

NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
ALTERATIONS = ['', 'b', '#']
WTF_NOTES = ['B#', 'E#', 'Fb', 'Cb']


SCALES = ['melodic_minor', 'major', 'harmonic_minor', 'mixolydian', 'dorian', 'lydian', 'major_pentatonic', 'phrygian', 'natural_minor', 'minor_pentatonic', 'locrian']

for n in NOTES:
	for alt in ALTERATIONS:
		note = Note(n+alt)
		if str(note) in WTF_NOTES:
			continue
		for s in SCALES:
			scale_name = s.replace('_', ' ')
			front = 'The %s scale of %s is...' % (scale_name, str(note))
			back = ' '.join(map(str, scale(note, s)))

			print '\t'.join([front, back])