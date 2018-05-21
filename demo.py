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

audio_types = ('*.mp3', '*.m4a', '*.ogg', '*.wav')
vid_types = ('*.mp4', '*.mov', '*.mkv', '*.avi', '*.wmv')
pic_types = ('*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.psd')

print('Would you like to move... \n1. Audio \n2. Video \n3. Photos')
selection = (input("Enter a number 1, 2, or 3: "))
if int(selection) is 1:
	media_type = audio_types
else:
	if int(selection) is 2:
		media_type = vid_types
	else:
		if int(selection) is 3:
			media_type = pic_types
		else:
			print ('ENTER 1, 2, OR 3!')

dir_new = os.path.dirname(dird + '/! wish/')
if not os.path.exists(dir_new):
	os.makedirs(dir_new)

#After a random selection of files up to the desired amount is moved into the new folder
#... this function measures how much space is left and grabs the largest file that fills
#... the empty space. It's called repeatedly until the max desired size is reached'
def gap_fill(dird, limit, dir_new):
	korn = 0
	filez_left = []
	for i in media_type:
		filez_left.extend(glob.glob(dird + i))
	dir_new2 = glob.glob(dir_new + '/*')
	for i in dir_new2:
		zet = os.path.getsize(i)
		korn += zet
	xyz = limit - korn
	print('This is the amount of space left ' + str(xyz) + '\n')
	dicto = {}
	for i in filez_left:
		q = os.path.getsize(i)
		if q < xyz:
			dicto[i] = q
	hello = (max(dicto, key=dicto.get))
	hello_size = (os.path.getsize(hello))
	print ('The size of the file added is ' + str(hello_size))
	print ('I added this file ' + hello)
	os.rename(hello, dir_new + '/' + hello[chew:])


full = 0
filez = []
for i in media_type:
	filez.extend(glob.glob(dird + i))
for i in range(999):
	random.shuffle(filez)
	for i in range(1):
		pather = filez.pop()
	size = os.path.getsize(pather)
	full += size
	if full > limit:
		print('\n')
		while 111 == 111:
			try:
				gap_fill(dird, limit, dir_new)
			except ValueError:
				break
		print('That\'s all I could fit. \nYour ' + str(args['s']) + 'MB of files were placed in a folder called \'! wish\'')
		break
	else:
		print('I added this file ' + str(pather))
		os.rename(pather, dir_new + '/' + pather[chew:])
		del pather


