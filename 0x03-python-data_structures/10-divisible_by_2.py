#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiples_of_2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples_of_2.append(True)
        else:
            multiples_of_2.append(False)
    return (multiples_of_2)
