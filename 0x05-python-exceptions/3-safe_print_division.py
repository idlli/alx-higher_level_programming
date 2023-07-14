#!/usr/bin/python3
def safe_print_division(a, b):
    print('Inside result: ', end='')
    res = None
    try:
        res = a / b
        print('{:.1f}'.format(res))
    except ZeroDivisionError:
        print('{}'.format(None))
    finally:
        return res
