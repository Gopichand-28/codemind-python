def palindrome_check(num):
    a=str(num)
    b=int(a[::-1])
    if num==b:
        return True
    else:
        return False
n=int(input())
if palindrome_check(n):
    print('True')
else:
    print('False')
    

