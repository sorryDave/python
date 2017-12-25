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
	
	
def print_menu():
	print (
	"""
	MENU
	___________________
	
	1. New File
	2. Add to existing File
	3. Read file
	4. quit

	"""
	)
	
	
def create_file( file_name):
	print("Escriba su texto:\n")
	with open(file_name, 'w') as file:
		text = write_input()
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
	
	
def write_input():
	lines_ary = []
	while True:
		line = input()
		if line:
			lines_ary.append(line)
		else:
			break
	text = '\n'.join(lines_ary)
	return text
	
def main_p():
	while True:
		print_menu()
		option = input("option: ")
		if option == '1':
			name = input('name: ')
			menu(name,'w')
		elif option =='2':
			name = input('name: ')
			menu(name, 'a')
		elif option == '3':
			name = input('name: ')
			menu(name, 'r')
		elif option == '4':
			print('exit program')
			while True:
				opt = input('are you sure [y/n]')
				if opt == 'y':
					return # exits script
				elif opt == 'n':
					break
				else:
					print("no valid")
			

			
main_p()
# menu('newf.txt', 'w')
# menu('newf.txt','r')
# menu('newf.txt','a')
# menu('newf.txt','nx')
