import os

# file_name = ' '
file_mode_list = ['w', 'r', 'a']

################################################################
# Open a file
#fo = open("foo.txt", "wb")
#print ("Name of the file: ", fo.name)
#print ("Closed or not : ", fo.closed)
#print ("Opening mode : ", fo.mode)
#fo.close()
###############################################################


# placeholder
#def show(file_name, file_mode):
#    fmode = mode(file_mode)
#    if file_mode in file_mode_list:
#        print("\nfile: {}\nmode: {}, {}".format(repr(file_name), file_mode, fmode))
#    else:
#        print("\n{} is not included".format(file_mode))

# menu functions***************************************************
def menu(file_name, file_mode):
    #show(file_name, file_mode)
    if file_mode == 'w':
        create_file(file_name)
    elif file_mode == 'r':
        read_file(file_name)
    elif file_mode == 'a':
        append_file(file_name)
    elif file_mode == 'e':
        erase_file(file_name)
    elif file_mode == 'd':
        delete_file(file_name)


def print_menu():
    print(
        """
        MENU
        ___________________
    
        1. New File
        2. erase file
        3. Add to existing File
        4. Read file
        5. Delete file
        6. quit
        
        """
    )
# main create / write / delete / append / quit functions
def create_file(file_name):
    # get working directory
    path = os.getcwd()
    # scan dir
    scandir = os.scandir(path)
    for entry in scandir:
        if entry.name == file_name:
            print("\n\n\t found file with the same name: '{}' \n\n stop process".format(file_name))
    print("\nEscriba su texto: ")
    with open(file_name, 'w') as file:
        text = take_input()
        file.write(text)
    return text

def read_file(file_name):
    # get working directory
    path = os.getcwd()
    # scan dir
    scandir = os.scandir(path)
    for entry in scandir:
        if entry.name == file_name:
            print("\n\n\t found file with the same name: '{}'".format(file_name))
    with open(file_name, 'r') as file:
        text = file.read()
        print(text)
    #return text


def append_file(file_name):
    # get working directory
    path = os.getcwd()
    # scan dir
    scandir = os.scandir(path)
    for entry in scandir:
        if entry.name == file_name:
            print("\n\n\t found file with the same name: '{}'".format(file_name))
    print("\nEscriba su texto: ")
    with open(file_name, 'a') as file:
        text = take_input()
        file.write("\n" + text)
    return text

def erase_file(file_name):
    # get working directory
    path = os.getcwd()
    # scan dir
    scandir = os.scandir(path)
    for entry in scandir:
        if entry.name == file_name:
            print("\n\n\t found file with the same name: '{}' \n\n stop process".format(file_name))
    print("\nEscriba su texto: ")
    f =  open(file_name, 'w')
    f.close()

def delete_file(file_name):
    pass


def scan_dir():
    pass


# functiones***********************************************************************
def mode(mode):
    if mode == 'w':
        return 'write'
    elif mode == 'r':
        return 'read'
    elif mode == 'a':
        return 'append'

def take_input():
    lines_ary = []
    while True:
        line = input()
        if line:
            lines_ary.append(line)
        else:
            break
    text = '\n'.join(lines_ary)
    return text

# main**************************************************************
def main_p():
    while True:
        print_menu()
        option = input("option: ")
        if option == '1':
            name = input('name: ')
            menu(name, 'w')
        elif option == '2':
            name = input('name: ')
            menu(name, 'e')
        elif option == '3':
            name = input('name: ')
            menu(name, 'a')
        elif option == '4':
            name = input('name: ')
            menu(name, 'r')
        elif option == '5':
            name = input('name: ')
            menu(name, 'd')
        elif option == '6':
            print('exit program')
            while True:
                opt = input('are you sure [y/n] ')
                if opt == 'y':
                    return  # exits script
                elif opt == 'n':
                    break
                else:
                    print("no valid")


main_p()
