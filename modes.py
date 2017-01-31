from musthe import Note, Interval, scale

NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
WTF_NOTES = ['B#', 'E#', 'Fb', 'Cb']
ALTERATIONS = ['', 'b', '#']

MODES = [
	{'name': 'ionian', 'interval': 'P1', 'chord': 'maj7', 'tag': ''}, 
	{'name': 'dorian', 'interval': 'M2', 'chord': '-7', 'tag': ''}, 
	{'name': 'phrygian', 'interval': 'M3', 'chord': None, 'tag': ''}, 
	{'name': 'lydian', 'interval': 'P4', 'chord': 'maj7#11', 'tag': ''}, 
	{'name': 'mixolydian', 'interval': 'P5', 'chord': '7', 'tag': ''}, 
	{'name': 'aeolian', 'interval': 'M6', 'chord': '-6', 'tag': ''}, 
	{'name': 'locrian', 'interval': 'M7', 'chord': '-7b5', 'tag': ''}
]


for n in NOTES:
	for alt in ALTERATIONS:
		note = Note(n+alt)
		if str(note) in WTF_NOTES:
			continue
		mode_index = 1
		for m in MODES:
			interval = Interval(m['interval'])
			mode_note = note+interval
			# Scale
			front = 'From which <b style="color:red">major scale</b> comes %s %s ?' % (str(mode_note), m['name'])
			back = '<h1>'+str(note) + ' (#' + str(mode_index) + ' degree)</h1>'
			mode_index += 1
			print '\t'.join([front, back, 'mode-scale'])

			# Chord
			if not m['chord']:
				continue
			front = 'Which <b style="color:blue">chord</b> is associated to %s %s ?' % (str(mode_note), m['name'])
			back = '<h1>'+str(mode_note)+m['chord']+'</h1>'
			print '\t'.join([front, back, 'mode-chord'])

