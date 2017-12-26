import os

# file_name = ' '
file_mode_list = ['w', 'r', 'a']


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
        return 'append'


def print_menu():
    print(
        """
        MENU
        ___________________
    
        1. New File
        2. Add to existing File
        3. Read file
        4. quit
        
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
    print("Escriba su texto:\n")
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
    print("Escriba su texto:\n")
    with open(file_name, 'r') as file:
        text = file.read()
        print(text)
    #return text

        
# appen no funciona. escribe sin salto de linea
def append_file(file_name):
    # get working directory
    path = os.getcwd()
    # scan dir
    scandir = os.scandir(path)
    for entry in scandir:
        if entry.name == file_name:
            print("\n\n\t found file with the same name: '{}'".format(file_name))
    print("Escriba su texto:\n")
    with open(file_name, 'a') as file:
        text = take_input()
        file.write(text)
    return text

def delete_file():
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
            menu(name, 'a')
        elif option == '3':
            name = input('name: ')
            menu(name, 'r')
        elif option == '4':
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
# menu('newf.txt', 'w')
# menu('newf.txt','r')
# menu('newf.txt','a')
# menu('newf.txt','nx')