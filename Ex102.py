"""102. Write a Python program to get system command output."""
import subprocess


def get_syscmd_output(command):
    returned_text = subprocess.check_output(command, shell=True, universal_newlines=True)
    return returned_text


print(get_syscmd_output('dir'))