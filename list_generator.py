from random import randint


def list_generator(length, type):
    list = [None] * length

    #random
    if type == 'random':
        for i in range(length):
            list[i] = randint(0, 100)

    #increasing
    if type == 'increasing':
        for i in range(length):
            list[i] = randint(0, 100)
        list.sort()

    #decreasing
    if type == 'decreasing':
        for i in range(length):
            list[i] = randint(0, 100)
        list.sort(reverse=True)

    #constant
    if type == 'constant':
        for i in range(length):
            list[i] = int(1)

    #v-shape
    if type == 'v-shape':
        half_length = int(length / 2)
        left_list = [None] * half_length
        for i in range(half_length):
            left_list[i] = randint(0, 100)
        left_list.sort(reverse=True)
        right_list = left_list[:]
        right_list.sort()
        list = left_list + right_list

    return list
