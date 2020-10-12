"""97. Write a Python program to list the special variables used within the language."""

## copied solution
system_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print()
print( '\n'.join(' '.join(system_var_names[i:i+8]) for i in range(0, len(system_var_names), 8)) )
print()
