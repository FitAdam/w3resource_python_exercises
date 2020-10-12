"""76. Write a Python program to get the command-line arguments 
(name of the script, the number of arguments, arguments) passed to a script"""


import argparse

def script():
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="string will be multiplied and displayed")
    args = parser.parse_args()

    for x in range(100):
        print(args.echo)
    return print('done')



script()