#file_name = ' '
file_mode_list=['w', 'r','a']

#placeholder
def show(file_name, file_mode):
	fmode = mode(file_mode)
	if file_mode in file_mode_list:
		print( "\nfile: {}\nmode: {}, {}".format(repr(file_name), file_mode, fmode))
	else:
		print("\n{} is not included".format(file_mode))
	
def menu(file_name, file_mode):
	show(file_name,file_mode)
	if file_mode == 'w':
		create_file(file_name)
	elif file_mode == 'r':
		read_file(file_name)
	elif file_mode == 'a':
		append_text(file_name)
		return 'append'
	
	
		
def create_file( file_name):
	print("Escriba su texto:\n")
	with open(file_name, 'w') as file:
		text = write()
	return text
	
def mode(mode):
	if mode == 'w':
		return 'write'
	elif mode == 'r':
		return 'read'
	elif mode == 'a':
		return 'append'

def append_text(file_name):
	print("\tappend")
	
	
	
def read_file(file_name):
	print("\treading")
	
	
def write():
	lines_ary = []
	while True:
		line = input()
		if line:
			lines_ary.append(line)
		else:
			break
	text = '\n'.join(lines_ary)
	return text
	
menu('newf.txt', 'w')
menu('newf.txt','r')
menu('newf.txt','a')
menu('newf.txt','nx')
