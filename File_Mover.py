import os
import uuid
import glob
import random
import argparse

parser = argparse.ArgumentParser();
parser.add_argument('-i', type=str, help='Path to the files this script will select from.', required=True)
parser.add_argument('-s', type=int, help='Amount in MB of files you\'d like.', required=True)
args = vars(parser.parse_args())

MB = 1000000
GB = 1000000000
limit = args['s'] * MB
dird = args['i']
chew = len(dird)

print('Would you like to move... \n1. Videos \n2. Music \n3. Photos')
while True:
	try:
		selection = int(input("\nEnter a number 1, 2, or 3: "))
	except ValueError:
		print('I said enter the number 1, 2, or 3')
		continue
	if selection is 0:
		print('I said enter the number 1, 2, or, 3')
		continue
	if selection > 3:
		print('I said enter the number 1, 2, or, 3')
		continue
	else:
		break

if selection is 1: #VIDEO
	media_type = ('*.mp4', '*.mov', '*.mkv', '*.avi', '*.wmv')
else:
	if selection is 2: #AUDIO
		media_type = ('*.mp3', '*.m4a', '*.ogg', '*.wav')
	else:
		if selection is 3: #PHOTOS
			media_type = ('*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.psd')


dir_new = os.path.dirname(dird + '/! wish/')
if not os.path.exists(dir_new):
	os.makedirs(dir_new)

#After a random selection of files up to the desired amount is moved into the new folder
#... this function measures how much space is left and grabs the largest file that fills
#... the empty space. It's called repeatedly until the max desired size is reached'
def gap_fill(dird, limit, dir_new):
	ice = 0
	filez_left = []
	for i in media_type:
		filez_left.extend(glob.glob(dird + i))
	dir_new2 = glob.glob(dir_new + '/*')
	for i in dir_new2:
		snow = os.path.getsize(i)
		ice += snow
	xyz = limit - ice
	print('This is the amount of space left ' + str(xyz) + '\n')
	dicto = {}
	for i in filez_left:
		q = os.path.getsize(i)
		if q < xyz:
			dicto[i] = q
	hello = (max(dicto, key=dicto.get))
	hello_size = (os.path.getsize(hello))
	print ('The size of the file added is ' + str(hello_size))
	print ('\nI squeezed in this file ' + hello)
	os.rename(hello, dir_new + '/' + hello[chew:])


full = 0
filez = []
for i in media_type:
	filez.extend(glob.glob(dird + i))
for i in range(999):
	random.shuffle(filez)
	for i in range(1):
		panther = filez.pop()
	size = os.path.getsize(panther)
	full += size
	if full > limit:
		print('\n')
		while True:
			try:
				gap_fill(dird, limit, dir_new)
			except ValueError:
				break
		print('That\'s all I could fit. \nYour ' + str(args['s']) + 'MB of files were placed in a folder called \'! wish\'')
		break
	else:
		print('I added this file ' + str(panther))
		os.rename(panther, dir_new + '/' + panther[chew:])
		#del panther


