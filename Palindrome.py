m=int(input())
def palindrome_check(num):
    a=str(num)
    b=int(a[::-1])
    if num==b:
        print('True')
    else:
        print('False')

palindrome_check(m)