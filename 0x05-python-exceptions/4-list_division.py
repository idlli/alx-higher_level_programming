#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        div = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            div = a / b
        except IndexError:
            print('out of range')
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        finally:
            result.append(div)
    return result
