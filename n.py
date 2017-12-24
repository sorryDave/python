import sys


# f_name = 'new.txt'
f_mode = 'w'

# creating a path:
path = '/home/hellodave/filenew.txt'
 # path.join(f_name)
print(path)

# open append() mode ("a")
# f.tell() returns an integer current pos
# f.read(5) reads 5 char
# f.seek(offset, from what) 1 current position 2 end of the file
def open_file(file_name, file_mode):
    print("Escriba el text\n")
    with open(file_name,file_mode) as file:
        texto = lines()
        file.write(texto)

        #lines = []
        #while True:
        #    line = input()
        #    if line:
        #        lines.append(line)
        #    else:
        #        break
        #text = '\n'.join(lines)

        #######################################################
        #print("Enter/Paste your content. Ctrl-D to save it.")
        #contents = []
        #while True:
        #    try:
        #        line = input()
        #    except EOFError:
        #        break
        #    contents.append(line)
        #
        #
        #
        #
        #######################################################
        #lines = sys.stdin.readlines()
        #
        #lines = [line for line in sys.stdin]
        #
        #five_lines = list(itertools.islice(sys.stdin, 5))
        #
        #######################################################



    if file.closed:
        print("file Closed\n")

def lines():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    return text


def append_file(file_name):
    print("añadir texto:\n")
    with open(file_name,'a') as file:
        texto = lines()
        file.write(texto)


def read_file():
    with open( '/home/hellodave/filenew.txt', 'r') as file:
        content = file.read()
    print(content)




def print_menu():
    print(
    """
    MENU:
    ------------
    1.New file
    2.Write file
    3.Read file
    4.Quit
    
    
    write an option [1/2/3/4]: 
    """
    )

def menu():
    while True:
        print_menu()
        option = input('[1/2/3/4 : ')
        if option == '1':
            open_file(path, f_mode)
        elif option == '2':
            append_file(path)
        elif option == '3':
            read_file()
        elif option == '4':
            print("exit")
            break
        else:
            "Please enter a valid option : "



menu()



