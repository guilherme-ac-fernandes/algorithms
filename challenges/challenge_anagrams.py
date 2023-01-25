# Função Merge Sort recursivo proveniente do site Code Review
# source: https://codereview.stackexchange.com/questions/9732
# 0/recursive-and-iterative-approach-for-mergesort
def mergesort_recur(seq):
    if not seq:
        return []
    if len(seq) == 1:
        return [seq[0]]
    middle = len(seq) // 2
    left = mergesort_recur(seq[0:middle])
    right = mergesort_recur(seq[middle:len(seq)])
    return merge_recur(left, right)


def merge_recur(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    if lst1[0] > lst2[0]:
        return [lst2[0]] + merge_recur(lst1, lst2[1:])
    else:
        return [lst1[0]] + merge_recur(lst1[1:], lst2)


def is_anagram(first_string, second_string):
    first_array = mergesort_recur(first_string.lower())
    second_array = mergesort_recur(second_string.lower())
    first_order = ''.join(first_array)
    second_order = ''.join(second_array)

    if first_string == '' or second_string == '':
        return (first_order, second_order, False)

    for index, _ in enumerate(first_array):
        if first_array[index] != second_array[index]:
            return (first_order, second_order, False)
    return (first_order, second_order, True)
