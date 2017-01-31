import os
from musthe import Note, Interval, scale

NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
ALTERATIONS = ['', 'b', '#']

for n in NOTES:
	for alt in ALTERATIONS:
		note = Note(n+alt)
		minor_relative = note + Interval('M6')

		alt_name = 'natural'
		if alt == 'b':
			alt_name = 'flat'
		elif alt == '#':
			alt_name = 'sharp'

		tag = '-'.join(['key', alt_name])
		file_name = '-'.join([n, alt_name, 'major'])+'.png'
		file_path = os.getcwd()+'/keys/'+file_name
		img_html = '<img src="'+file_name+'"/>'

		if not os.path.exists(file_path):
			continue

		# Front img / back scale
		back = '<h1>'+str(note)+' major / '+str(minor_relative)+' minor</h1>'
		tags = ' '.join([tag, 'key-img'])
		print '\t'.join([img_html, back, tags])

		# Front scale / back img
		front = '<h1>'+str(note)+' major</h1>'
		tags = ' '.join([tag, 'key-major'])
		print '\t'.join([front, img_html, tags])

		front = '<h1>'+str(minor_relative)+' minor</h1>'
		tags = ' '.join([tag, 'key-minor'])
		print '\t'.join([front, img_html, tags])