def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) <= 1:
        return True
    if looking_str[0] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:-1])


print(is_palindrome('o'))
print(is_palindrome('sassas'))
print(is_palindrome('mom'))
print(is_palindrome('momo'))