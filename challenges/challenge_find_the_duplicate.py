def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    numbers = sorted(nums)
    for index, num in enumerate(numbers[:-1]):
        if not isinstance(num, int) or num < 0:
            return False
        if num == numbers[index + 1]:
            return num
    return False
