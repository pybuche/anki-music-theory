from musthe import Note, Interval

NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
WTF_NOTES = ['B#', 'E#', 'Fb', 'Cb']
ALTERATIONS = ['', 'b', '#']

INTERVALS = {
	'm2': {'label': 'minor 2nd', 'tag': 'middle'},
	'M2': {'label': 'major 2nd', 'tag': 'easy'},
	'm3': {'label': 'minor 3rd', 'tag': 'easy'},
	'M3': {'label': 'major 3rd', 'tag': 'easy'},
	'P4': {'label': 'perfect 4th', 'tag': 'middle'},
	'A4': {'label': 'augmented 4th', 'tag': 'hard'},
	'd5': {'label': 'diminished 5th', 'tag': 'hard'},
	'P5': {'label': 'perfect 5th', 'tag': 'easy'},
	'A5': {'label': 'augmented 5th', 'tag': 'hard'},
	'm6': {'label': 'minor 6th', 'tag': 'middle'},
	'M6': {'label': 'major 6th','tag': 'middle'},
	'd7': {'label': 'diminished 7th', 'tag': 'hardcore'},
	'm7': {'label': 'minor 7th', 'tag': 'middle'},
	'M7': {'label': 'major 7th', 'tag': 'middle'}
}

CHORDS_INTERVALS = {
	'9': 'M2',
	'b9': 'm2',
	'11': 'P4',
	'#11': 'A4',
	'13': 'M6',
	'b13': 'm6'
}



def get_tag(interval_tag, answer):
	if len(answer) > 2 or answer in WTF_NOTES:
		return 'hardcore'
	return interval_tag


for n in NOTES:
	for alt in ALTERATIONS:
		note = Note(n+alt)
		if str(note) in WTF_NOTES:
			continue

		for (interval_code, interval_data) in INTERVALS.iteritems():
			interval = Interval(interval_code)
			answer = note+interval

			front = 'The %s of %s is...' % (interval_data['label'], str(note))
			back = '<h1>'+str(answer)+'</h1>'
			answer_tag = get_tag(interval_data['tag'], str(answer))
			tags = ' '.join([answer_tag, 'interval'])
			print '\t'.join([front, back, tags])

		for (interval_name, interval_code) in CHORDS_INTERVALS.iteritems():
			interval = Interval(interval_code)
			octave = Interval('P8') 
			answer = note+interval+octave

			front = 'The %s of %s is...' % (interval_name, str(note))
			back = '<h1>'+str(answer)+'</h1>'
			answer_tag = get_tag('hard', str(answer))
			tags = ' '.join([answer_tag, 'chord-interval'])
			print '\t'.join([front, back, 'tags'])
