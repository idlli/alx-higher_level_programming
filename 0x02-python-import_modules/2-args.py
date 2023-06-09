#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv
    if len(argv) == 1:
        print('0 arguments.')
    else:
        if len(argv) == 2:
            print('{} argument:'.format(len(argv) - 1))
        else:
            print('{} arguments:'.format(len(argv) - 1))
        for i, arg in list(enumerate(argv))[1:]:
            print('{}: {}'.format(i, arg))
