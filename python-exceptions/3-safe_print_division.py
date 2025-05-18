#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        cuocient = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(cuocient))
    return cuocient
