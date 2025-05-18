#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            cuocient = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            cuocient = 0
        except ZeroDivisionError:
            print("division by 0")
            cuocient = 0
        except IndexError:
            print("out of range")
            cuocient = 0
        finally:
            new_list.append(cuocient)
    return new_list
