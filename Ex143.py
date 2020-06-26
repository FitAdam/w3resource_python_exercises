"""143. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system."""

import platform
import sys

print(platform.architecture(executable=sys.executable, bits='', linkage=''))
print(platform.node())