def is_palindrome_iterative(word):
    if len(word) == 0:
        return False

    start = 0
    end = len(word) - 1

    while start <= end:
        print(word[start], word[end])
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            return False
    return True
