"""100. Write a Python program to get the name of the host on which the routine is running. """

import socket

def get_name():
    print('The host name is: ')
    return print(socket.gethostname())


get_name()

