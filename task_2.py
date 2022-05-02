#2.Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50). Выведите на
# экран исходный и отсортированный массивы.

import random

def merge_sort(array):

    def merge(first, second):
        res = []
        i, j = 0, 0

        while i < len(first) and j < len(second):

            if first[i] < second[j]:
                res.append(first[i])
                i += 1

            else:
                res.append(second[j])
                j += 1

        res.extend(first[i:] if i < len(first) else second[j:])

        return res

    def div_half(array):

        if len(array) == 1:
            return array

        elif len(array) == 2:
            return array if array[0] <= array[1] else array[::-1]

        else:
            return merge(div_half(array[:len(array)//2]), div_half(array[len(array)//2:]))

    return div_half(array)


size = 20
min_item = 0
max_item = 50
array = [random.uniform(min_item, max_item) for _ in range(size)]

print('Исходный массив:', array, sep='\n')
print('Отсортированный массив:', merge_sort(array), sep='\n')

