def isPalindrome(x: int) -> bool:
    # Более быстрое решение
    if x < 0:
        return False
    invert_number = 0
    change_num = x
    while change_num > 0:
        invert_number = invert_number * 10 + change_num % 10
        change_num = change_num // 10
    return invert_number == x
    # Простое решение
    # return str(x) == str(x)[::-1]

print(isPalindrome(101))
print(isPalindrome(1011))
print(isPalindrome(-121))


