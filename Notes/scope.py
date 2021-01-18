my_name = 'sille'

def print_local_name():
    my_name = 'Ell'
    # local scoped variable, does not affect global variable
    print('My name is', my_name)

def print_new_global_name():
    global my_name
    my_name = 'Ellis'
    # adding 'global (variable_name)' redefines global variable
    print('My name is', my_name)