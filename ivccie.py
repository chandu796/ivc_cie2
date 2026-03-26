n = int(input())

s = 0
while n > 0:
    s += n % 10
    n //= 10

rev = int(str(s)[::-1])

if s == rev:
    print("palindrome")
else:
    print("not palindrome")