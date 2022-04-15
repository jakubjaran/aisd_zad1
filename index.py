import time
import pandas

from list_generator import list_generator

from insertion_sort import insertion_sort
from selection_sort import selection_sort
from heap_sort import heap_sort
from merge_sort import merge_sort


def test_sort_func(sort_func, list):
    list_copy = list[:]
    start = time.time()
    sort_func(list_copy)
    end = time.time()
    elapsed = end - start
    return elapsed


def main():
    print("List length:")
    list_length = int(input())

    print("Step:")
    step = int(input())

    print("List type (random, increasing, decreasing, constant, v-shape):")
    list_type = input()

    writer = pandas.ExcelWriter(f'out/{list_type}_{list_length}_{step}.xlsx',
                                engine='openpyxl')
    N = []
    IS = []
    SS = []
    HS = []
    MS = []

    for i in range(0, 15 * step, step):
        print(f'List length: {list_length + i}')
        list = list_generator(list_length + i, list_type)
        N.append(list_length + i)
        IS.append(test_sort_func(insertion_sort, list))
        SS.append(test_sort_func(selection_sort, list))
        HS.append(test_sort_func(heap_sort, list))
        MS.append(test_sort_func(merge_sort, list))

    data = pandas.DataFrame({'N': N, 'IS': IS, 'SS': SS, 'HS': HS, 'MS': MS})
    data.to_excel(writer, sheet_name=f'{list_type}', index=False)
    writer.save()


main()
