#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4 as hidden_4
    for name in filter(lambda i: not i.startswith('__'), dir(hidden_4)):
        print(name)
