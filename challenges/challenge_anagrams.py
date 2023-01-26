# Função Merge Sort recursivo proveniente do site Code Review
# source: https://codereview.stackexchange.com/questions/9732
# 0/recursive-and-iterative-approach-for-mergesort
def merge_sort(string):

    if not string:
        return []

    if len(string) == 1:
        return [string[0]]

    middle = len(string) // 2
    left = merge_sort(string[0:middle])
    right = merge_sort(string[middle:len(string)])

    return merge(left, right)


def merge(part_one, part_two):

    if not part_one:
        return part_two

    if not part_two:
        return part_one

    if part_one[0] > part_two[0]:
        return [part_two[0]] + merge(part_one, part_two[1:])
    else:
        return [part_one[0]] + merge(part_one[1:], part_two)


def is_anagram(first_string, second_string):

    first_array = merge_sort(first_string.lower())
    second_array = merge_sort(second_string.lower())

    first_order = ''.join(first_array)
    second_order = ''.join(second_array)

    if first_string == '' or second_string == '':
        return (first_order, second_order, False)

    for index, _ in enumerate(first_array):
        if first_array[index] != second_array[index]:
            return (first_order, second_order, False)

    return (first_order, second_order, True)
