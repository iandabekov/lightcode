def is_palindrome(s):
    if len(s) < 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
a = str(input("Введите строку:"))
if (is_palindrome(a) == True):
    print("Данная строка палиндром!")
else:
    print("Данная строка не палиндром!")
