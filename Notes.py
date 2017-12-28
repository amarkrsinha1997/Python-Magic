#!python3
#!usr/bin/python3.6
 import pyperclip,datetime,sys


if (sys.argv<2):
	print('Error Insufficient arguments')
	print('Usage: python3.6 Notes.py [argument](write or read)')
	sys.exit()
arg=sys.argv[1]
if arg=='write':
	file = open('Notes.txt','a+')

	notes= pyperclip.paste()
	date=datetime.now().strftime("%Y-%m-%d %H:%M")
	file.write(date+'\n'+notes+'\n')

	file.close()
elif arg=='read':
	file = open('Notes.txt','r+')
	notes = file.readlines()
	pyperclip.copy(notes[0:2])
	del notes[0:2]
	file.write(notes)
	file.close()