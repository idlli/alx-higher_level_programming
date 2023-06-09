#!/usr/bin/python3
def no_c(my_string):
    return ''.join(filter(lambda c: c not in 'cC', my_string))
