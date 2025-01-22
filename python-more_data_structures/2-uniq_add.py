#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    seen = set()

    for elem in my_list:
        if elem not in seen:
            seen.add(elem)
            total += elem

    return total
